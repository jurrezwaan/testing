<center><div class="readability"><h1 id="exercise-testing">Exercise: Testing</h1>
<p>This is it! We are letting go of <code>wincpy check</code>. From now on, you will be writing your own tests. This exercise helps you on your way.</p>
<p>One popular method for writing good code is to <em>first</em> write the tests, and only <em>then</em> write the function that should pass those tests. This way of doing
software development is called <code class="interpreted-text" role="term">Test-Driven Development</code> (<code class="interpreted-text" role="term">TDD</code>), and it's the way
this exercise will be structured.</p>
<p>First, create a simple folder structure to work with, for example:</p>
<blockquote>
<pre class=""><code>testing
├── main.py
└── test_main.py</code></pre></blockquote>
<h2 id="part-1">Part 1</h2>
<ol type="1">
<li>In <code>test_main.py</code>, write a function <code>test_get_none</code> that tests if a function from <code>main.py</code> called <code>get_none</code> returns
<code>None</code>.</li>
<li>In <code>main.py</code>, write the function <code>get_none</code> that should take no arguments and always return <code>None</code>.</li>
</ol>
<p>This dummy example is a practical application of test-driven development; first we write the test, <em>then</em> the function that is being tested.</p>
<h2 id="part-2">Part 2</h2>
<ol type="1">
<li>
<p>In <code>test_main.py</code>, write a function <code>test_flatten_dict</code> that tests if a function <code>flatten_dict</code>, when given a dictionary (<code>dict</code>) as
its argument, returns the values of that dictionary in a list (<code>list</code>). For example:</p>
<div class="sourceCode" id="cb2">
<pre class="sourceCode python"><code class="sourceCode python"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>flatten_dict({<span class="st">'a'</span>: <span class="dv">42</span>, <span class="st">'b'</span>: <span class="fl">3.14</span>})</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="co"># [42, 3.14]</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>flatten_dict({<span class="st">'a'</span>: [<span class="dv">42</span>, <span class="dv">350</span>], <span class="st">'b'</span>: <span class="fl">3.14</span>})</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="co"># [[42, 350], 3.14]</span></span></code></pre></div>
<div class="tip">
<div class="title">
<p>Tip</p>
</div>
<p>Try to think about the tests you're writing as a tiered system. First you might test if the value returned by <code>flatten_dict</code> is a list at all. Then you could test
the function with a very small (single element) dictionary, then more complex dictionaries. This way, if a test fails, you not only now <em>that</em> it fails, but also exactly
<em>where</em> it fails. The more granular your testing tiers, the better you can trace the bug if the test fails.</p>
</div>
</li>
<li>
<p>In <code>main.py</code>, implement the function <code>flatten_dict</code> so that it passes the tests you wrote in <code>test_flatten_dict</code>. Another example:</p>
<div class="sourceCode" id="cb3">
<pre class="sourceCode python"><code class="sourceCode python"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>flatten_dict({<span class="st">'a'</span>: {<span class="st">'inner_a'</span>: <span class="dv">42</span>, <span class="st">'inner_b'</span>: <span class="dv">350</span>}, <span class="st">'b'</span>: <span class="fl">3.14</span>})</span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="co"># [{'inner_a': 42, 'inner_b': 350}, 3.14]</span></span></code></pre></div>
<p>Run the tests you wrote with <code>pytest</code> as you are working on the implementation of the <code>flatten_dict</code> function.</p>
</li>
</ol>
<div class="note">
<div class="title">
<p>Note</p>
</div>
<p>For an extra challenge, see if you can implement <code>flatten_dict</code> in such a way that the dictionary is flattened all the way down regardless of how many nested levels
original dictionary contains. For example:</p>
<div class="sourceCode" id="cb4">
<pre class="sourceCode python"><code class="sourceCode python"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>flatten_dict({<span class="st">'a'</span>: {<span class="st">'inner_a'</span>: <span class="dv">42</span>, <span class="st">'inner_b'</span>: <span class="dv">350</span>}, <span class="st">'b'</span>: <span class="fl">3.14</span>})</span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a><span class="co"># [42, 350, 3.14]</span></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>flatten_dict({<span class="st">'a'</span>: [{<span class="st">'inner_inner_a'</span>: <span class="dv">42</span>}]})</span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a><span class="co"># [42]</span></span></code></pre></div>
<p>To do this you may want to look into a technique that is called <code class="interpreted-text" role="term">recursion</code>.</p>
</div></div></center>
