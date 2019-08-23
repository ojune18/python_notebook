def symmetrical(num):
    try:

        int(num)

        original_str = str(num)

        return original_str[::-1] == original_str

    except Exception as ex:
        print("Error => ", ex.message)


if __name__ == "__main__":

    print(symmetrical(input("Enter a number for symmetrical test\n")))

#
# def get_permutations(word):
#     # single word permutations
#     if len(word) <= 1:
#         return set(word)
#
#     # solve smaller problem recursively
#     smaller_perms = get_permutations(word[1:])
#
#     # find all permutation by inserting the first character
#     # to each position of each smaller permutation
#     perms = set()
#     for small_perm in smaller_perms:
#         print(small_perm)
#         for pos in range(0, len(small_perm) + 1):
#             perm = small_perm[:pos] + word[0] + small_perm[pos:]
#             perms.add(perm)
#     return perms
#
#
# print(get_permutations("nan"))
