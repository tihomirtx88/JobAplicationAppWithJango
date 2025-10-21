# Job Application Django App

This is a **Django web application** for managing job applications. The project allows users to register, log in, submit job applications through a form, and receive email confirmations. Admin users can manage all applications using Django's built-in admin panel.

---

## Features

### 1. User Authentication
- **Registration:** Users can create an account with a username, email, and password.
- **Login/Logout:** Authenticated users can log in and log out securely.
- **Session Management:** User sessions are maintained and protected.

### 2. Job Application Form
- **Fields:** First name, last name, email, date of availability, occupation.
- **Validation:** Form data is validated before submission.
- **Email Notification:** After submitting the form, a confirmation email is sent to the user.
- **Admin Panel Integration:** Submitted forms are stored in the database and can be managed in the Django admin panel.

### 3. Admin Panel
- **Django Admin:** Admins can view, edit, and delete submitted applications.
- **Customizations:**
  - Inline address management (if applicable)
  - Search, filters, and sorting
  - Read-only fields, list display, and pagination

### 4. Pages
- **Index Page:** Job application form.
- **About Page:** Information about the project or company.
- **Authentication Pages:** Login and register templates.
