# Day 3: Backend Basics, APIs & Full-Stack Overview
## Thursday Teaching Guide (2.5 Hours)

---

## 📋 Session Overview

**Date**: Thursday, February 5, 2026  
**Time**: 5:00 PM - 7:30 PM  
**Duration**: 2.5 hours  
**Focus**: Backend responsibilities, REST APIs, databases, authentication basics, and the full-stack roadmap

---

## 🎯 Learning Objectives

By the end of this session, students will be able to:
- Explain what backend does in a web app
- Describe what an API is and how REST works
- Understand CRUD operations and endpoints
- Differentiate SQL vs NoSQL databases
- Explain basic auth concepts (sessions vs tokens)
- Visualize full-stack architecture end-to-end
- Know next steps to become a full-stack developer

---

## 📚 Session Outline (2.5h)

| Time | Topic | Duration |
|------|-------|----------|
| 5:00-5:45 PM | What is Backend? & REST APIs | 45 min |
| 5:45-6:25 PM | Databases Basics (SQL vs NoSQL) | 40 min |
| 6:25-7:00 PM | Auth & Security Basics | 35 min |
| 7:00-7:20 PM | Full-Stack Architecture & Roadmap | 20 min |
| 7:20-7:30 PM | Final Project Introduction | 10 min |

---

## 🎓 Detailed Teaching Plan

### Part 1: What is Backend? & REST APIs (5:00 - 5:45)

**Backend Responsibilities:**
```
✅ Authentication & Authorization
✅ Business logic (rules, calculations)
✅ Data validation (serious checks)
✅ Database operations (CRUD)
✅ Integrations (payments, email)
✅ Security (rate limiting, input sanitization)
```

**What Backend Is Not:**
```
❌ Designing buttons/colors (frontend job)
❌ Handling click events in browser
❌ Storing data only in memory (needs persistence)
```

**API Definition:**
> API = A contract that lets one program talk to another. For web: usually HTTP endpoints returning JSON.

**REST Concepts:**
- Resource-based (nouns): `/users`, `/tasks`, `/orders`
- Use HTTP methods for actions: GET/POST/PUT/PATCH/DELETE
- Stateless: each request has all info needed

**CRUD Mapping Example (Tasks):**
```
GET    /api/tasks        → List tasks
GET    /api/tasks/1      → Get single task
POST   /api/tasks        → Create task
PUT    /api/tasks/1      → Replace task
PATCH  /api/tasks/1      → Update part of task
DELETE /api/tasks/1      → Delete task
```

**Request/Response Example:**
```
Request: POST /api/tasks
Headers: Content-Type: application/json
Body:
{
  "title": "Buy milk",
  "done": false
}

Response: 201 Created
Headers: Content-Type: application/json
Body:
{
  "id": 42,
  "title": "Buy milk",
  "done": false
}
```

**Hands-On Demo (Conceptual):**
- Use `jsonplaceholder.typicode.com/todos` in browser/Thunder Client
- Show GET request and JSON response
- Highlight status code and headers

---

### Part 2: Databases Basics (5:45 - 6:25)

**Why Databases:**
- Persistent storage
- Query/filter data fast
- Handle concurrent users

**SQL vs NoSQL:**
```
SQL (Relational)
├── Tables, rows, columns
├── Strong schemas
├── Joins
├── ACID transactions
└── Examples: PostgreSQL, MySQL

NoSQL (Document/Key-Value)
├── Flexible schemas
├── Store JSON-like docs
├── Scale horizontally easily
└── Examples: MongoDB, DynamoDB
```

**When to Use What:**
- SQL: structured data, relationships (orders, users)
- NoSQL: flexible/fast iteration (logs, JSON docs)

**Example Schemas:**
```sql
-- SQL: tasks table
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  done BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW()
);
```

```json
// NoSQL (MongoDB): tasks collection document
{
  "_id": "507f1f77bcf86cd799439011",
  "title": "Buy milk",
  "done": false,
  "createdAt": "2026-02-05T17:00:00Z"
}
```

**Where DB Fits:**
```
Browser (frontend)
   ↓ HTTP
Backend (API server)
   ↓ DB queries
Database (stores data)
```

**Demo (Conceptual):**
- Show how an API would respond with data pulled from DB
- Emphasize backend is the gatekeeper to DB

---

### Part 3: Auth & Security Basics (6:25 - 7:00)

**Auth Concepts:**
- Authentication = Who are you?
- Authorization = What can you do?

**Sessions vs Tokens:**
```
Sessions (Cookies)
├── Server stores session data
├── Cookie holds session ID
├── Common in traditional web apps

Tokens (JWT)
├── Server issues signed token
├── Client stores token (usually in memory/localStorage)
├── Sent in Authorization header
├── Good for APIs/mobile
```

**JWT (High-Level):**
- JSON Web Token: header.payload.signature
- Signed, not encrypted (don't put passwords inside)
- Client sends `Authorization: Bearer <token>`

**HTTPS Reminder:**
- Always use HTTPS in production
- Protects tokens and cookies

**Minimal Flow (Conceptual):**
```
Login:
Client → POST /api/login (email+password)
Server:
  - Validate
  - Create JWT { userId }
  - Return token
Client stores token

Authenticated request:
Client → GET /api/tasks with Header: Authorization: Bearer <token>
Server verifies token → returns data
```

**Security Basics to Mention:**
- Validate inputs on backend
- Hash passwords (bcrypt), never store plain text
- Rate limiting (prevent abuse)
- CORS basics for APIs

---

### Part 4: Full-Stack Architecture & Roadmap (7:00 - 7:20)

**Full-Stack Diagram:**
```
Browser (HTML/CSS/JS)
   ↓ fetch/axios
API Server (Node/Express, Django, Laravel)
   ↓ SQL/NoSQL queries
Database (PostgreSQL/MySQL/MongoDB)
```

**Data Flow Example (Task App):**
```
1) User adds task in UI → JS calls POST /api/tasks
2) Backend validates and stores in DB
3) UI fetches tasks with GET /api/tasks
4) UI renders list from JSON
```

**Learning Roadmap (High-Level):**
1. **Frontend**: HTML → CSS → JS → Framework (React/Vue)
2. **Backend**: Node/Express (or Django/Laravel) → REST APIs
3. **Database**: SQL first (PostgreSQL/MySQL), then explore NoSQL
4. **Git/GitHub**: Version control and collaboration
5. **Deployment**: Vercel/Netlify for frontend, Render/Heroku for backend
6. **Projects**: Build 2-3 full-stack apps for portfolio

---

### Part 5: Final Project Intro (7:20 - 7:30)

**Simple Full-Stack Task List (Overview):**
- Frontend: HTML/CSS/JS form + list
- Backend: Simple JSON API (can use json-server or small Node/Express)
- Data: Tasks with `id`, `title`, `done`
- Actions: Add task, list tasks (stretch: toggle done)

**Minimal API Spec:**
```
GET    /api/tasks      → list tasks
POST   /api/tasks      → add task { title }
PATCH  /api/tasks/:id  → toggle done (optional)
DELETE /api/tasks/:id  → remove (optional)
```

**Submission:**
- ZIP or GitHub link
- Screenshot of working app

Tell students: Full details in FINAL_PROJECT guide.

---

## 📊 Teaching Tips for Day 3

- Keep concepts high-level; avoid deep DB/Admin setup
- Use diagrams for API flow and auth
- Reuse the restaurant analogy (backend = kitchen, DB = pantry)
- If time is tight, prioritize API + CRUD + auth overview
- Emphasize security best practices simply: HTTPS, hashing, validate input

### Common Pitfalls
- Confusing authentication vs authorization
- Thinking JWT = encryption (it is not; it's signed)
- Forgetting that backend guards the DB (frontend never talks to DB directly)

### If Ahead of Time
- Demo a tiny Node/Express server returning JSON
- Show a quick Postman/Thunder Client call

### If Behind Time
- Shorten SQL vs NoSQL deep dive
- Skip optional auth details; keep it conceptual

---

## ✅ Success Checklist

After Day 3, students should:
- [ ] Explain backend role and REST APIs
- [ ] Map CRUD to HTTP methods
- [ ] Differentiate SQL vs NoSQL at a high level
- [ ] Understand sessions vs tokens conceptually
- [ ] Visualize full-stack data flow
- [ ] Know the next steps on the roadmap

---

## 📝 Materials to Prepare

- Simple API examples (jsonplaceholder endpoints)
- Optional: tiny Express server sample
- Diagrams for REST, auth, and DB placement
- Roadmap slide/visual
- Final project spec ready to share

---

**Day 3 connects the dots—students see the full-stack picture and how to continue learning. 🌐**
