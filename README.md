# pynomad

Unofficial Python client for HashiCorp Nomad.

## Why

I'm a fan of Python and a fan of Nomad. In using Nomad, I started to pick up a little Go and really came
to appreciate the power of structs. Looking around, I didn't really see a client library that talked to Nomad
and gave back something like a struct.

So, having used Pydantic with other projects, I wanted to see what it would look like to create a client library for Nomad
that returned (where appropriate) Pydantic models that somewhat mimic the experience of working with Go structs.

### Pydantic

Honestly, I could probably figure out a good chunk of this via standard dataclasses, but having used Pydantic, I really
like some of the niceties that it gives you (looking at your `.dict()` and `.json()`!).

There may be other projects out there, but I haven't used them enough to feel like I want to use them here.

