Instagram Challenge
===================

The Problem
-----------

On their [blog][1] Instagram's engineering team recently posted a small [Python challenge][2] to win a T-Shirt.  

Inspired by their in-office paper shredder, the team came up with the problem of reconstructing the shredded image (below) into it's original form.

![The Shredded Image][3]

On their [blog][2], they post advice about using [Python's Imaging Library, PIL][4] to solve the problem as well as a few other guidelines and tips.

The Solution
------------

So, I had a go at solving this particular problem, and this GitHub repository contains the source code I came up with.  Unfortunately, so far I have failed - this is the closest I can get to an unshredded image:

![The Unshredded Image][5]

Although all the strips or shreds are correctly sorted, the resulting image is wrapped and so is incorrect.  Answers on a postcard!  It should of course look like this:

![The Real Unshredded Image][6]

Follow Up
---------

Since posting this, a number of other people have hit the same problem.  Others (such as [Fatty Beagle][7]) have got around this by sampling surrounding pixel data rather than using absolute values of the outer most strips; by using a graph traversal to more reliably establish the outer most strips (as demonstrated by [The Sociable][8]), or through a combination of techniques involving changing colour spaces and introducing thresholds ([Shatter Mediocrity][9]).  Some have even solved it using [HTML5][10].  

I have decided not to update my code and leave it as-is, because having now seen these alternative approaches I'm not up for plagiarism.

Want more?  [DARPA][11] in the U.S. have posted a challenge to reconstruct shredded text based documents for intelligence purposes.  Solved in 33 days by a team of 3 developers, the bounty of $50k was slightly more than the t-shirt offered by the Instagram guys. 

[1]: http://instagram-engineering.tumblr.com/
[2]: http://instagram-engineering.tumblr.com/post/12651721845/instagram-engineering-challenge-the-unshredder
[3]: https://github.com/mstreatfield/instagram/raw/master/images/source.png
[4]: http://www.pythonware.com/products/pil/index.htm
[5]: https://github.com/mstreatfield/instagram/raw/master/images/unshredded_fail.png
[6]: https://github.com/mstreatfield/instagram/raw/master/images/unshredded.png
[7]: http://www.fattybeagle.com/2011/11/22/instagram-engineering-challenge/
[8]: https://bitbucket.org/thesociable/instagram/src/78343e3a4
[9]: http://shattermediocrity.com/post/12816649382/the-instagram-challenge
[10]: http://feval.info/instagram/canvas.html
[11]: http://challenge.gov/DoD/254-darpa-s-shredder-challenge
