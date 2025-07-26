document.addEventListener("DOMContentLoaded", () => {
  const toggleBtn = document.getElementById("toggle-theme");
  const input = document.getElementById("markdown-input");
  const preview = document.getElementById("preview");

  // Load dark mode preference
  if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark");
  }

  toggleBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    const theme = document.body.classList.contains("dark") ? "dark" : "light";
    localStorage.setItem("theme", theme);
  });

  input.addEventListener("input", () => {
    const rawText = input.value;
    preview.innerHTML = markdownToHTML(rawText);
  });

  function markdownToHTML(md) {
    // Simple markdown-like converter (for demo)
    return md
      .replace(/^### (.*$)/gim, "<h3>$1</h3>")
      .replace(/^## (.*$)/gim, "<h2>$1</h2>")
      .replace(/^# (.*$)/gim, "<h1>$1</h1>")
      .replace(/\*\*(.*)\*\*/gim, "<b>$1</b>")
      .replace(/\*(.*)\*/gim, "<i>$1</i>")
      .replace(/\n$/gim, "<br />");
  }
});
const saveBtn = document.getElementById("save-post");
const titleInput = document.getElementById("post-title");
const postList = document.getElementById("post-list");

// Load saved posts on startup
const savedPosts = JSON.parse(localStorage.getItem("posts") || "{}");
renderPostList();

saveBtn.addEventListener("click", () => {
  const title = titleInput.value.trim();
  const content = input.value;

  if (!title || !content) {
    alert("Title and content are required!");
    return;
  }

  savedPosts[title] = content;
  localStorage.setItem("posts", JSON.stringify(savedPosts));
  renderPostList();
  alert("✅ Post saved!");
});

function renderPostList() {
  postList.innerHTML = "";
  for (const title in savedPosts) {
    const li = document.createElement("li");
    li.textContent = title;
    li.style.cursor = "pointer";
    li.addEventListener("click", () => {
      titleInput.value = title;
      input.value = savedPosts[title];
      preview.innerHTML = markdownToHTML(savedPosts[title]);
    });
    postList.appendChild(li);
  }
}
