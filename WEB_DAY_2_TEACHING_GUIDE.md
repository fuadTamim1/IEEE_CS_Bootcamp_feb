# Day 2: Frontend Essentials (Enough to Start)
## Tuesday Teaching Guide (2.5 Hours)

---

## 📋 Session Overview

**Date**: Tuesday, February 3, 2026  
**Time**: 5:00 PM - 7:30 PM  
**Duration**: 2.5 hours  
**Focus**: HTML structure, CSS layout, JavaScript interaction, and calling APIs with fetch

---

## 🎯 Learning Objectives

By the end of this session, students will be able to:
- Build basic webpages with semantic HTML
- Use forms, inputs, and buttons to capture user data
- Apply CSS for layout and spacing using the Box Model
- Create responsive layouts with Flexbox
- Manipulate the DOM with JavaScript
- Handle events (click, input, submit)
- Fetch data from a public API using `fetch()`
- Render JSON data into the UI

---

## 📚 Session Outline (2.5h)

| Time | Topic | Duration |
|------|-------|----------|
| 5:00-5:45 PM | HTML — Structure & Semantics | 45 min |
| 5:45-6:25 PM | CSS — Box Model & Flexbox | 40 min |
| 6:25-7:00 PM | JavaScript — DOM & Events | 35 min |
| 7:00-7:20 PM | Frontend → Backend Flow (fetch) | 20 min |
| 7:20-7:30 PM | Mini Practice & Wrap-up | 10 min |

---

## 🎓 Detailed Teaching Plan

### Part 1: HTML — Structure & Semantics (5:00 - 5:45)

**Key Concepts:**
- HTML = structure (skeleton)
- Tags, attributes, nesting
- Semantic elements: `header`, `nav`, `main`, `section`, `article`, `footer`
- Forms: `form`, `input`, `button`, `label`

**Live Coding: Basic Page**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simple Page</title>
</head>
<body>
  <header>
    <h1>My First Web Page</h1>
    <nav>
      <a href="#home">Home</a>
      <a href="#about">About</a>
      <a href="#contact">Contact</a>
    </nav>
  </header>

  <main>
    <section id="home">
      <h2>Welcome</h2>
      <p>This is a simple example page.</p>
    </section>

    <section id="signup">
      <h2>Sign Up</h2>
      <form id="signup-form">
        <label for="name">Name</label>
        <input id="name" name="name" placeholder="Your name" required>

        <label for="email">Email</label>
        <input id="email" name="email" type="email" placeholder="you@example.com" required>

        <button type="submit">Submit</button>
      </form>
    </section>
  </main>

  <footer>
    <small>© 2026 Web Workshop</small>
  </footer>
</body>
</html>
```

**Teaching Tips:**
- Explain `required`, `type="email"` validation
- Show nesting and indentation
- Show `id` vs `class` (id = unique, class = reusable)

**Exercise (5 min):** Add another section called "Features" with a list of three items.

---

### Part 2: CSS — Box Model & Flexbox (5:45 - 6:25)

**Key Concepts:**
- Box Model: content, padding, border, margin
- Display types: block, inline, inline-block
- Flexbox basics: container + items
- Responsive: mobile-first mindset

**Live Coding: Add CSS**
```html
<style>
  :root {
    --bg: #0f172a;
    --card: #111827;
    --text: #e5e7eb;
    --accent: #38bdf8;
  }

  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: "Inter", system-ui, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.5;
  }

  header, main, footer {
    max-width: 960px;
    margin: 0 auto;
    padding: 24px;
  }

  nav a {
    color: var(--accent);
    margin-right: 12px;
    text-decoration: none;
    font-weight: 600;
  }

  section {
    background: var(--card);
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 16px;
    border: 1px solid rgba(255,255,255,0.05);
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  input {
    padding: 12px;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.15);
    background: #0b1220;
    color: var(--text);
  }

  button {
    padding: 12px;
    border: none;
    border-radius: 8px;
    background: var(--accent);
    color: #0b1220;
    font-weight: 700;
    cursor: pointer;
  }

  /* Flexbox example */
  .features {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
  }
  .feature-card {
    flex: 1 1 200px;
    padding: 16px;
    border-radius: 10px;
    background: #0c1324;
    border: 1px solid rgba(255,255,255,0.06);
  }
</style>
```

**Flexbox Demo:**
- `.features` as flex container
- `.feature-card` items wrap on small screens
- Show resizing the browser

**Exercise (5 min):** Add three feature cards with titles and short text.

---

### Part 3: JavaScript — DOM & Events (6:25 - 7:00)

**Key Concepts:**
- JS runs in browser
- DOM selection: `document.querySelector`
- Events: `addEventListener`
- Updating text and classes
- Prevent default on forms

**Live Coding: Handle Form Submit**
```html
<script>
  const form = document.getElementById('signup-form');
  const nameInput = document.getElementById('name');
  const emailInput = document.getElementById('email');

  form.addEventListener('submit', (event) => {
    event.preventDefault(); // stop page reload

    const name = nameInput.value.trim();
    const email = emailInput.value.trim();

    if (!name || !email) {
      alert('Please fill in all fields');
      return;
    }

    // Show success message
    alert(`Thanks, ${name}! We received: ${email}`);

    // Clear form
    form.reset();
  });
</script>
```

**Exercise (5 min):** Add real-time validation: if email is empty, add a red border; remove it when filled.

---

### Part 4: Frontend → Backend Flow (fetch) (7:00 - 7:20)

**Key Concepts:**
- `fetch(url)` returns a Promise
- `response.json()` parses JSON
- Handling loading and errors
- Rendering data into the DOM

**Live Demo: Fetch from Public API (JSONPlaceholder)**
```html
<section id="posts">
  <h2>Latest Posts</h2>
  <button id="load-posts">Load Posts</button>
  <div id="posts-list"></div>
</section>

<script>
  const loadBtn = document.getElementById('load-posts');
  const postsList = document.getElementById('posts-list');

  loadBtn.addEventListener('click', async () => {
    postsList.innerHTML = '<p>Loading...</p>';
    try {
      const res = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=5');
      if (!res.ok) throw new Error('Network error');
      const data = await res.json();

      postsList.innerHTML = data.map(post => `
        <article class="feature-card">
          <h3>${post.title}</h3>
          <p>${post.body}</p>
        </article>
      `).join('');
    } catch (err) {
      postsList.innerHTML = `<p style="color:#f87171">Error: ${err.message}</p>`;
    }
  });
</script>
```

**Explain:**
- GET request
- Status codes via `res.ok`
- JSON parsing
- Render to DOM with `innerHTML`

**Exercise (5 min):** Change `_limit=5` to `_limit=3` and show only titles as a list.

---

### Part 5: Mini Practice & Wrap-up (7:20 - 7:30)

**Mini Practice (Choose One, 7 min):**
1) Build a simple "Quote Loader" button that fetches one quote from https://api.quotable.io/random and displays it.
2) Add a new input field "Favorite color" and when submitted, show a colored badge with that color.

**Wrap-up (3 min):**
- Review: HTML structure, CSS layout, JS events, fetch
- Connect to tomorrow: "Next we see the backend side, APIs, databases, auth, and the full-stack picture."

---

## 📊 Teaching Tips for Day 2

- Keep coding visible; type slowly
- Use Live Server for instant reloads
- Show DevTools Console for errors
- Demo responsiveness by resizing window
- Reinforce separation of concerns (HTML vs CSS vs JS)
- Celebrate when fetch succeeds (students love live data!)

### Common Pitfalls
- Forgetting to prevent form submission reload
- CORS errors (explain quickly if arise)
- Mixed content (http vs https) — use https APIs
- Typos in query selectors

### If Ahead of Time
- Introduce CSS Grid briefly
- Add simple input validation messages under fields
- Show `fetch` POST example (mock) with `jsonplaceholder`

### If Behind Time
- Shorten CSS deep dive; focus on Flexbox
- Skip optional exercises, assign as homework

---

## ✅ Success Checklist

After Day 2, students should:
- [ ] Build a semantic HTML page
- [ ] Style with CSS and Flexbox
- [ ] Handle form submissions with JS
- [ ] Manipulate the DOM
- [ ] Fetch and display JSON data
- [ ] Understand frontend → backend flow

---

## 📝 Materials to Prepare

- Starter HTML/CSS/JS files
- JSONPlaceholder endpoints ready
- Live Server extension installed
- Backup HTML/CSS snippets
- A few screenshots/gifs of expected UI

---

**Day 2 gets students building real pages and talking to APIs—keep it hands-on and visual! 🌐**
