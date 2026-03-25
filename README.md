<style>
   :root {
      --bg: #0f172a;
      --card: #111827;
      --text: #e5e7eb;
      --muted: #9ca3af;
      --accent: #22c55e;
      --accent-soft: #1f2937;
      --border: #374151;
   }

   .readme-wrap {
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      line-height: 1.6;
      color: var(--text);
      background: linear-gradient(180deg, #0b1220 0%, #111827 100%);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 28px;
      margin: 8px 0;
   }

   .title {
      margin: 0;
      font-size: 2rem;
      color: #f9fafb;
   }

   .subtitle {
      margin-top: 8px;
      color: var(--muted);
   }

   .badge {
      display: inline-block;
      margin: 10px 8px 0 0;
      padding: 6px 12px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: var(--accent-soft);
      color: #d1fae5;
      font-size: 0.85rem;
   }

   .card {
      margin-top: 20px;
      padding: 16px;
      border: 1px solid var(--border);
      border-radius: 10px;
      background: rgba(17, 24, 39, 0.75);
   }

   .card h2 {
      margin-top: 0;
      color: #f3f4f6;
      border-left: 4px solid var(--accent);
      padding-left: 10px;
   }

   .toc a {
      color: #93c5fd;
      text-decoration: none;
   }

   .toc a:hover {
      text-decoration: underline;
   }

   ul {
      margin: 8px 0 0 20px;
   }

   code,
   pre {
      font-family: "Fira Code", Consolas, monospace;
   }

   pre {
      background: #0b1020;
      border: 1px solid #253047;
      border-radius: 8px;
      padding: 14px;
      overflow-x: auto;
      color: #d1d5db;
   }

   .warning {
      border-left: 4px solid #f59e0b;
      padding: 10px 12px;
      background: rgba(245, 158, 11, 0.1);
      border-radius: 6px;
      color: #fde68a;
   }

   .footer-note {
      margin-top: 18px;
      color: var(--muted);
      font-size: 0.92rem;
   }
</style>

<div class="readme-wrap">
   <h1 class="title">Information Security Ciphers in Python</h1>
   <p class="subtitle">
      A practical Information Security project that demonstrates classic cryptography algorithms in Python: Caesar, Playfair,
      Rail Fence, Vigenère, and a simple XOR-based Stream Cipher.
   </p>

   <span class="badge">Python 3.8+</span>
   <span class="badge">Cryptography Learning</span>
   <span class="badge">No External Dependencies</span>

   <div class="card toc">
      <h2>Table of Contents</h2>
      <ul>
         <li><a href="#project-overview">Project Overview</a></li>
         <li><a href="#cipher-implementations">Cipher Implementations</a></li>
         <li><a href="#project-structure">Project Structure</a></li>
         <li><a href="#requirements">Requirements</a></li>
         <li><a href="#how-to-run">How to Run</a></li>
         <li><a href="#example-usage">Example Usage</a></li>
         <li><a href="#educational-note">Educational Note</a></li>
         <li><a href="#how-to-make-this-publicly-available">How to Make This Publicly Available</a></li>
         <li><a href="#license">License</a></li>
      </ul>
   </div>

   <div class="card" id="project-overview">
      <h2>Project Overview</h2>
      <p>
         This project contains command-line Python programs for text encryption and decryption, including educational
         step-by-step output and key-based/transposition-based workflows.
      </p>
   </div>

   <div class="card" id="cipher-implementations">
      <h2>Cipher Implementations</h2>
      <ul>
         <li><strong>Caesar Cipher</strong> — <code>CeaserCipher.py</code> — substitution by fixed shift key.</li>
         <li><strong>Playfair Cipher</strong> — <code>PlayfairCipher.py</code> — digraph substitution using 5x5 key matrix.</li>
         <li><strong>Rail Fence Cipher</strong> — <code>RailfnceCipher.py</code> — transposition via zig-zag rails.</li>
         <li><strong>Stream Cipher (XOR)</strong> — <code>StreamCipher.py</code> — repeated key-byte XOR encryption.</li>
         <li><strong>Vigenère Cipher</strong> — <code>VigenereCipher.py</code> — polyalphabetic substitution with repeating key.</li>
      </ul>
   </div>

   <div class="card" id="project-structure">
      <h2>Project Structure</h2>
      <pre><code>.
├── CeaserCipher.py
├── PlayfairCipher.py
├── RailfnceCipher.py
├── StreamCipher.py
├── VigenereCipher.py
└── README.md</code></pre>
   </div>

   <div class="card" id="requirements">
      <h2>Requirements</h2>
      <ul>
         <li>Python 3.8+ recommended</li>
         <li>No third-party packages required</li>
      </ul>
   </div>

   <div class="card" id="how-to-run">
      <h2>How to Run</h2>
      <pre><code>python3 CeaserCipher.py
python3 PlayfairCipher.py
python3 RailfnceCipher.py
python3 StreamCipher.py
python3 VigenereCipher.py</code></pre>
   </div>

   <div class="card" id="example-usage">
      <h2>Example Usage</h2>
      <ul>
         <li>Enter plaintext/ciphertext when prompted.</li>
         <li>Provide the required key (shift, word key, or rail count).</li>
         <li>Select encryption (<code>e</code>) or decryption (<code>d</code>).</li>
         <li>Review formatted output/tables generated by the script.</li>
      </ul>
   </div>

   <div class="card" id="educational-note">
      <h2>Educational Note</h2>
      <p class="warning">
         These are classic ciphers for learning cryptography fundamentals and are not secure for modern production communication.
      </p>
   </div>

   <div class="card" id="how-to-make-this-publicly-available">
      <h2>How to Make This Publicly Available</h2>
      <ol>
         <li>Create a new public GitHub repository.</li>
         <li>Push your project:</li>
      </ol>
      <pre><code>git init
git add .
git commit -m "Add classic cipher implementations"
git branch -M main
git remote add origin https://github.com/&lt;your-username&gt;/&lt;your-repo&gt;.git
git push -u origin main</code></pre>
      <ol start="3">
         <li>In repository settings, set visibility to Public and add relevant topics.</li>
         <li>Optional: Add badges, social preview image, and SEO-friendly description.</li>
      </ol>
   </div>

   <div class="card" id="license">
      <h2>License</h2>
      <p>Use an MIT License for open educational use by adding a <code>LICENSE</code> file.</p>
   </div>

   <p class="footer-note">
      Keywords: Information Security, Cryptography, Python Cipher Project, Caesar Cipher, Playfair Cipher, Rail Fence Cipher,
      Vigenere Cipher, Stream Cipher XOR, Encryption, Decryption, Cybersecurity Learning.
   </p>
</div>
