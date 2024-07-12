<h1>Facebook Profile Scraper</h1>

<p>This project scrapes information from a specified Facebook profile URL and stores the data in a JSON file. The scraper is scheduled to run every day at 10:30 PM IST using GitHub Actions.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#setup">Setup</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#github-actions">GitHub Actions</a></li>
    <li><a href="#license">License</a></li>
</ul>

<h2 id="setup">Setup</h2>

<ol>
    <li><strong>Clone the repository</strong>:
        <pre><code>git clone https://github.com/csn1101/facebook-scraper.git
cd facebook-scraper</code></pre>
    </li>
    <li><strong>Create a virtual environment</strong>:
        <pre><code>python -m venv scraper_project</code></pre>
    </li>
    <li><strong>Activate the virtual environment</strong>:
        <ul>
            <li>On Windows:
                <pre><code>scraper_project\Scripts\activate</code></pre>
            </li>
            <li>On macOS/Linux:
                <pre><code>source scraper_project/bin/activate</code></pre>
            </li>
        </ul>
    </li>
    <li><strong>Install the required Python packages</strong>:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Update the <code>config.json</code> file</strong> with the Facebook profile URL you want to scrape.</li>
</ol>

<h2 id="usage">Usage</h2>

<p>To run the scraper manually, use the following command:</p>
<pre><code>python scraper/scraper.py</code></pre>

<h2 id="github-actions">GitHub Actions</h2>

<p>The scraper is scheduled to run automatically every day at <strong>10:30 PM IST</strong> using GitHub Actions. The workflow file is located at <code>.github/workflows/scraper.yml</code>.</p>

<h2 id="license">License</h2>

<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

