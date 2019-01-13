import numpy as np
import scipy.stats as st

n = 100000

# print("Normal 0.0",
#     max(
#         abs(
#             st.uniform.cdf(np.linspace(0, 1, n), 0, 1.) - st.gennorm.cdf(np.linspace(0, 1, n), 1.6, loc=0.5, scale=0.5))
#     )
# )
# print("Normal 0.0", max(abs(st.uniform.cdf(np.linspace(0, 1, n), 0, 1.) - st.gennorm.cdf(np.linspace(0, 1, n), 30, loc=0.4, scale=0.5))))
# print("Normal 0.0", max(abs(st.uniform.cdf(np.linspace(0, 1, n), 0, 1.) - st.gennorm.cdf(np.linspace(0, 1, n), 30, loc=0.5, scale=0.4))))

print("H1 distance", max(abs(st.uniform.cdf(np.linspace(0, 1, n), 0, 1.) - st.beta.cdf(np.linspace(0, 1, n), 1.22, 0.9))))
print("H2 distance", max(abs(st.uniform.cdf(np.linspace(0, 1, n), 0, 1.) - st.beta.cdf(np.linspace(0, 1, n), 1., 0.75))))
print("H3 distance", max(abs(st.uniform.cdf(np.linspace(0, 1, n), 0, 1.) - st.beta.cdf(np.linspace(0, 1, n), 0.8, 1.08))))

print("H4 distance", max(abs(st.uniform.cdf(np.linspace(0, 1, n), 0, 1.) - st.gennorm.cdf(np.linspace(0, 1, n), 8, loc=0.5, scale=0.5))))
print("H5 distance", max(abs(st.uniform.cdf(np.linspace(0, 1, n), 0, 1.) - st.gennorm.cdf(np.linspace(0, 1, n), 8, loc=0.45, scale=0.5))))
print("H6 distance", max(abs(st.uniform.cdf(np.linspace(0, 1, n), 0, 1.) - st.gennorm.cdf(np.linspace(0, 1, n), 8, loc=0.5, scale=0.4))))

