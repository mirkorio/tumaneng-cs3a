import streamlit as st

st.header("Primitive Root")

def get_inputs():
    q = st.number_input("Enter the prime number (q):", min_value=2, step=1)
    g = st.number_input("Enter the candidate primitive root (g):", min_value=1, step=1)
    return q, g

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primitive(g, p):
    primitive_roots = []
    for i in range(1, p):
        temp = set()
        output = ''
        j = 1
        while j < p:
            result = pow(i, j, p)
            output += f"{i}^{j} mod {p} = {result}"
            if j < p - 1:
                output += ", "
            temp.add(result)
            if result == 1:
                break
            j += 1
        if len(temp) == p - 1:
            primitive_roots.append(i)
            output += f" ==> {i} is primitive root of {p}, "
        st.write(output)
    if g in primitive_roots:
        return True, primitive_roots
    else:
        return False, primitive_roots

def main():
    q, g = get_inputs()
    if prime(q):
        is_primitive_root, primitive_roots = check_primitive(g, q)
        print_result(q, g, is_primitive_root, primitive_roots)
    else:
        st.write(f"{q} is not a prime number!!")

def print_result(q, g, is_primitive_root, primitive_roots):
    if is_primitive_root:
        st.write(f"{g} is a primitive root of {q}. Primitive roots: {primitive_roots}")
    else:
        st.write(f"{g} is NOT a primitive root of {q}. Primitive roots: {primitive_roots}")

if __name__ == "__main__":
    main()
