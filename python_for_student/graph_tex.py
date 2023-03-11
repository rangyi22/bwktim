#graph_tex.py
# https://matplotlib.org/tutorials/text/mathtext.html
import matplotlib.pyplot as plt
import numpy as np

print(plt.style.available) # pyplot module에서 가능한 graphic style들
plt.style.use('ggplot')
t = np.arange(0, 1, 0.01)
plt.plot(t, np.sin(2*np.pi*t))
plt.title(r'$\alpha > \beta$')
plt.text(0.15, 0.5,  \
    r'$\alpha_i, \beta_, \gamma, \Gamma, \pi, \Pi, \phi, \theta$')
plt.text(0.15, 0, r'$nC_k = \frac{n!}{k!(n-k)!}$  and \     
              $\lim_{x \to \infty} e^{-x} = 0$', fontsize=11)
plt.text(0.15, -0.5, \
       r'$2 \times \sum_{n=0}^\infty \frac{-e^{i\pi}}{2^n}$')
plt.show()
