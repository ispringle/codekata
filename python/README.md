# CodeKata

## Install

`pip install -r requirements.txt`

## Usage

`python codekata {challenge_number} {day}`

## Challenge One

Challenge one is not an actual "coding" code kata, instead it is a mental
exercise. I might eventually do a write-up of my thoughts on that challenge,
but for the time being the `one.py` module is merely boilerplate for the
other days, allowing me to do `cp one.py two.py`.

## Challenge Two

### Day One

There is a pretty simple and basic implementation. I didn't encounter any
issues other than I got the `>` mixed up for the `m = e` branch of the if
statement. Fixed that and then it ran just fine. Little concerned that I won't
have four more ways to write this!

### Day Two

I thought this would be simple. But no matter what I did I kept hitting my head
against the spectre of infinitely looping recursion. The way I ended up
finding this bug was by walking through the chop in my head -- luckily this
function is basic enough that I could do this without trouble! Ended up
being that if `e` was equal to `0` then the `if not e` would kick in, and that
somehow short-circuited the following catch to return if `e == 0`.

### Day Three

I initially stumbled upon this idea yesterday but didn't have the mental power
to get it working -- I was also fixated on a recursive answer then... Decided
to give this a shot today, and boy this one proved to be easy to get _almost_
there and then a slog to get that last 1%. In fact, if not for my last test
with a huge, random list I would have never detected this problem because
it only snuck up on me over time. Basically an off-by-one over numberous
iterations. I solved that issue, which was due to `len(a) // 2` not always
being equal to `len(a) - (len(a) // 2)` (also it's needless work to do that,
and then had another issue when `len(a) // 2` has to floor the quotient to
return an `int`. Tracked that down, but I over did it, resulting in an
off-by-one for a whole other reason. But... problem solved!

### Day Four

Sorta cheated, it's day one, just oop-y. Created a SortedArray class and then
some methods to find the target. Used the computed attribute via the
`__getattr__` method for some added coolness and to make it more interesting,
but other than that, it's day one's... no errors or issues, worked on the my
first run of the tests.

### Day Five

I promise I wasn't stumped. I've had a hectic last few weeks of life. Had an
initial product deployment at work, followed by a marathon sprint to get in
some missing features before anyone notices. Plus, living on a farm means that
everyday is a busy day. And on top of that I've been interviewing for four or
five different positions. But onto day five...

Today's solution uses the std library. I think that is a valid solution, given
that it's a) there and b) probably a better tool for the job than to write one
yourself, at least IRL. Had to do a little logic to return the right value, as
the `biset.biset_left()` method returns the index value to _insert_ `t` and
not the location of `t` or `-1` if `t` is not in the array. Short, sweet,
correct.
