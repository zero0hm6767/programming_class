import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.integrate import cumulative_trapezoid

G = 1.0 # 重力定数(固定)

# =========================
#    宇宙物理学入門 課題5
#   (星の内部構造を求めよう)
# =========================

# =========================
#           注意
# =========================
# このノートブックは閲覧用です。直接編集をしてバグを仕込んだりすると，他の人にも影響が出ます。
# そのため，各自で左上の「ファイル」→「ドライブにコピーを保存」を選び，自分のGoogle Drive上のコピーを編集して使用してください。
#
# 左上の「▶︎」をクリックするとプログラムを実行できます。


# =========================
#  各自が変更できるパラメータ
# =========================

k     = 1.0      # P = k rho^gammaのk (温度に対応する変数)
gamma = 4.0/3.0      # 比熱比γ (必ず1.0以上を入れる。授業で扱った等温の場合はγ=1, 単原子分子理想気体の場合はγ=5/3, 星内部で使うことがあるのはγ=4/3)
rho_c = 1.0      # 中心の密度


# =========================
#       計算領域の設定
# =========================

r_min = 1.0e-5   # 計算する範囲(内側), 0にしてはいけない
r_max = 10.0     # 計算する範囲(外側)


# =========================
# r = 0付近での境界条件の設定 (気にしなくて良い)
# =========================

rho0 = rho_c - (2.0 * np.pi * G / (3.0 * k * gamma)) * rho_c**(3.0 - gamma) * r_min**2
q0 = - (4.0 * np.pi * G * rho_c / 3.0) * r_min**3

y0 = [rho0, q0]


# =========================
#     解くべき微分方程式
# =========================

def rhs(r, y):
    rho, q = y

    # 密度が負になってしまった場合の処理
    if rho <= 0:
        return [0.0, 0.0]

    drho_dr = q * rho**(2.0 - gamma) / (k * gamma * r**2)
    dq_dr = -4.0 * np.pi * G * r**2 * rho

    return [drho_dr, dq_dr]

def surface_event(r, y):
    rho, q = y
    return rho - 1.0e-8

surface_event.terminal = True
surface_event.direction = -1


# =========================
#        数値的に解く
# =========================

sol = solve_ivp(
    rhs,                   # 解くべき微分方程式
    t_span=(r_min, r_max), # 積分する範囲
    y0=y0,                 # 微分方程式の境界(初期)条件
    method="RK45",         # ルンゲクッタ法という手法で微分方程式を数値的に積分
    rtol=1.0e-8,           # 精度に関するパラメータ。気にしなくてよい
    atol=1.0e-10,          # 精度に関するパラメータ。気にしなくてよい
    dense_output=True,
    max_step=0.01,         # 精度に関するパラメータ。小さいほど精度がよくなるが，計算に時間がかかるようになる。
    events=surface_event
)


# =========================
#  得られた密度・圧力をプロット
# =========================

r = np.linspace(r_min, r_max, 2000)
rho = sol.sol(r)[0]
q = sol.sol(r)[1]

mask = rho > 0
r = r[mask]
rho = rho[mask]

P = k * rho**gamma
T = rho**(gamma - 1.0)

fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(r, rho, label=r"$\rho(r)$")
ax.plot(r, P, "--", label=r"$P(r)$")
ax.plot(r, T, ":", label=r"$T(r)$")

ax.set_xlabel(r"$r$")
ax.set_ylabel(r"density / pressure / temperature") # 密度:density, 圧力:pressure, 温度:temperature (それぞれ中心の値に対する比率)
ax.set_yscale("log")
ax.legend()

plt.tight_layout()
plt.show()


# =========================
#           発展
# =========================
# 星の表面半径 (便宜上，星の表面を「密度が中心密度の1/100となる半径」と定義)
r_surface = r[np.where(rho<rho_c*0.01)]
print("星の半径 : r = %e"%np.min(r_surface))

# 星の全質量
integrand = 4.0 * np.pi * r**2 * rho
M_r = cumulative_trapezoid(integrand, r, initial=0.0) # 球殻の質量 4πr^2 ρ を積分
M_star = M_r[-1]
print("星の質量 : M_star =", M_star)

# ビリアル定理が成立していることの確認
gamma_gas = 5.0 / 3.0
Pi = np.trapezoid(P * 4.0 * np.pi * r**2, r)
Phi = -np.trapezoid(
    G * M_r / r * 4.0 * np.pi * r**2 * rho,
    r
)
surface_term = 4.0 * np.pi * r[-1]**3 * P[-1]
print("ビリアル定理 : Phi + 3∫P dV - surface term =", Phi + 3.0 * Pi - surface_term)