"""f-strings and format specs: [[fill]align][sign][width][,][.precision][type]."""

name, qty, price = "widget", 3, 4.5
print(f"{name} x{qty} = ${qty * price:.2f}")
print(f"[{name:<10}] [{name:>10}] [{name:^10}] [{name:*^10}]")
print(f"{1234567.891:,.2f}  {0.256:.1%}  {255:#x}  {255:08b}  {42:+d}")
print(f"{qty=}  {price=}  {name!r}")
print(f"{'nested':>{qty + 5}}")

# str.format and % still exist.
print("{} is {}".format("pi", 3.14159), f"{3.14159:.3f}")
print("{0} {1} {0}".format("a", "b"), "%s-%03d" % ("id", 7))  # noqa: UP031

# A small table.
rows = [("apple", 3, 0.5), ("melon", 12, 2.25)]
for item, count, cost in rows:
    print(f"{item:<8}{count:>4}{cost:>8.2f}")
