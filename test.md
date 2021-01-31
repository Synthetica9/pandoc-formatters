---
formatters:
  nix: nixfmt
  haskell: brittany
---

# This is just a test

Should just format:

```{.nix}
{ foo
        }: foo
```

Should remain unchanged:

```{.nix .no-format}
{ foo
        }: foo
```

Should give an error, with original code intact:

```{.nix}
{
```

```haskell
foo :: Int


  -> Int
foo 0 = 0
foo 1 = 1
fib n = fib (n - 1) + fib (n - 2)
```
