# Diffie-Hellman Key Exchange Algorithm

# Function to perform modular exponentiation
def power_mod(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:  # If exp is odd, multiply base with result
            result = (result * base) % mod
        exp = exp >> 1  # Divide exp by 2
        base = (base * base) % mod  # Square the base
    return result

# Main Diffie-Hellman function
def diffie_hellman(p, g, private_a, private_b):
    # Calculate A's public key
    public_a = power_mod(g, private_a, p)

    # Calculate B's public key
    public_b = power_mod(g, private_b, p)

    # Calculate shared secret for both A and B
    shared_secret_a = power_mod(public_b, private_a, p)
    shared_secret_b = power_mod(public_a, private_b, p)

    return public_a, public_b, shared_secret_a, shared_secret_b

# Main program with input/output
if __name__ == "__main__":
    # Input: prime modulus p, generator g, private keys for A and B
    p = int(input("Enter a prime number p (e.g., 23): "))
    g = int(input("Enter a generator g (e.g., 5): "))
    private_a = int(input("Enter private key for A (e.g., 6): "))
    private_b = int(input("Enter private key for B (e.g., 15): "))

    # Perform Diffie-Hellman Key Exchange
    public_a, public_b, shared_secret_a, shared_secret_b = diffie_hellman(p, g, private_a, private_b)

    # Output the public keys and the shared secret
    print(f"\nPublic key of A: {public_a}")
    print(f"Public key of B: {public_b}")
    print(f"\nShared secret (calculated by A): {shared_secret_a}")
    print(f"Shared secret (calculated by B): {shared_secret_b}")

    # Check if both shared secrets match
    if shared_secret_a == shared_secret_b:
        print("\nKey exchange successful! Both parties share the same secret.")
    else:
        print("\nError! Shared secrets do not match.")
