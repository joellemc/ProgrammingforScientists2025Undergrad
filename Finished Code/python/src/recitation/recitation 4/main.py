"""
main.py — simple combination function with built-in tests.

First, install pytest
    pip install pytest (Windows)
    pip3 install pytest (macOS/Linux)

Run tests with:
    python -m pytest main.py (Windows)
    python3 -m pytest main.py (macOS/Linux)
"""

def combination(n: int, k: int) -> int:
    """Return C(n, k) with basic input validation."""
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("n and k must be integers")
    if n < 0 or k < 0:
        raise ValueError("n and k must be non-negative")
    if k > n:
        raise ValueError("k cannot be greater than n")

    # symmetry
    if k > n - k:
        k = n - k

    if k == 0 or k == n:
        return 1
    if k == 1:
        return n

    result = 1
    i = 1
    while i <= k:   
        result = (result * (n - k + i)) // i
        i = i + 1
    return result

def bray_curtis_distance(sample1, sample2):
    keys = set(sample1.keys()) | set(sample2.keys())

    numerator = 0
    denominator = 0

    for key in keys:
        a = sample1.get(key, 0)
        b = sample2.get(key, 0)
        numerator += abs(a - b)
        denominator += (a + b)

    # Handle edge case: both samples empty
    if denominator == 0:
        return 0.0

    return numerator / denominator

def jaccard_distance(sample1, sample2):
    keys = set(sample1.keys()) | set(sample2.keys())

    numerator = 0
    denominator = 0

    for key in keys:
        a = sample1.get(key, 0)
        b = sample2.get(key, 0)
        numerator += min(a, b)
        denominator += max(a, b)

    # Edge case: both empty
    if denominator == 0:
        return 0.0

    return 1 - numerator / denominator


# -------------------------
# Pytest tests live here too
# -------------------------

def test_combination_all():
    # Each tuple is (n, k, expected)
    cases = [
        (10, 0, 1),
        (10, 10, 1),
        (12, 1, 12),
        (8, 7, 8),
        (10, 4, 210),
        (10, 6, 210),
    ]

    i = 0
    while i < len(cases):   
        n, k, expected = cases[i]
        actual = combination(n, k)
        assert actual == expected, f"case {i} failed: C({n},{k})={actual}, expected {expected}"
        i = i + 1
    print("passed all tests!")

# -------------------------
# BC and Jaccard example tests
# -------------------------

def approx_equal(a, b, tol=1e-5):
    return abs(a - b) <= tol

def test_jaccard_sample1():
    s1 = {"coyotes": 499, "deer": 501}
    s2 = {"coyotes": 501, "deer": 499}
    assert approx_equal(jaccard_distance(s1, s2), 0.003992)

def test_jaccard_sample2():
    s1 = {"blue": 2, "green": 3, "purple": 1}
    s2 = {"purple": 1, "blue": 2, "green": 3}
    assert approx_equal(jaccard_distance(s1, s2), 0.0)

def test_jaccard_sample3():
    s1 = {"galaxy": 20, "brain": 12, "take": 17}
    s2 = {"I": 200, "don't": 14, "care": 99}
    assert approx_equal(jaccard_distance(s1, s2), 1.0)

def test_jaccard_sample4():
    s1 = {"bears": 4, "turkeys": 7, "coyotes": 0, "deer": 2, "groundhogs": 8}
    s2 = {"bears": 0, "turkeys": 5, "coyotes": 8, "deer": 4, "groundhogs": 6}
    assert approx_equal(jaccard_distance(s1, s2), 0.580645)

def test_jaccard_sample5():
    s1 = {"lions": 2, "tigers": 4}
    s2 = {"bears": 2, "lions": 4, "tigers": 3}
    assert approx_equal(jaccard_distance(s1, s2), 0.5)

def test_jaccard_sample6():
    s1 = {"bears": 2, "lions": 4, "tigers": 3}
    s2 = {"lions": 2, "tigers": 4}
    assert approx_equal(jaccard_distance(s1, s2), 0.5)


# -----------------------------
# Bray–Curtis distance tests
# -----------------------------
def test_bray_sample1():
    s1 = {"coyotes": 499, "deer": 501}
    s2 = {"coyotes": 501, "deer": 499}
    assert approx_equal(bray_curtis_distance(s1, s2), 0.002)

def test_bray_sample2():
    s1 = {"blue": 2, "green": 3, "purple": 1}
    s2 = {"purple": 1, "blue": 2, "green": 3}
    assert approx_equal(bray_curtis_distance(s1, s2), 0.0)

def test_bray_sample3():
    s1 = {"galaxy": 20, "brain": 12, "take": 17}
    s2 = {"I": 200, "don't": 14, "care": 99}
    assert approx_equal(bray_curtis_distance(s1, s2), 1.0)

def test_bray_sample4():
    s1 = {"bears": 4, "turkeys": 7, "coyotes": 0, "deer": 2, "groundhogs": 8}
    s2 = {"bears": 0, "turkeys": 5, "coyotes": 8, "deer": 4, "groundhogs": 6}
    assert approx_equal(bray_curtis_distance(s1, s2), 0.40909)

def test_bray_sample5():
    s1 = {"lions": 2, "tigers": 4}
    s2 = {"bears": 2, "lions": 4, "tigers": 3}
    assert approx_equal(bray_curtis_distance(s1, s2), 0.33333)

def test_bray_sample6():
    s1 = {"bears": 2, "lions": 4, "tigers": 3}
    s2 = {"lions": 2, "tigers": 4}
    assert approx_equal(bray_curtis_distance(s1, s2), 0.33333)