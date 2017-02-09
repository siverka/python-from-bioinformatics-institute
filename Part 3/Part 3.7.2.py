'''abcd
*d%#
abacabadaba
#*%*d*%
-----------
*d*%*d*#*d*
dacabac
'''


# from alpha
def translate(word: str, alpha: dict):
    return ''.join(alpha[e] for e in word)

alpha = input()
beta = input()

alpha_dict = {}
beta_dict = {}

for i in range(len(alpha)):
    alpha_dict[alpha[i]] = beta[i]
    beta_dict[beta[i]] = alpha[i]

atob = input()
btoa = input()

print(translate(atob, alpha_dict))
print(translate(btoa, beta_dict))
