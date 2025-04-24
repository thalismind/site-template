function secureCopy(text) {
  return new Promise((resolve, reject) => {
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(resolve).catch(reject);
    } else {
      reject(new Error("Clipboard API not available"));
    }
  });
}

function fallbackCopy(text) {
  return new Promise((resolve, reject) => {
    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.style.position = "fixed";  // Avoid scrolling to bottom
    textarea.style.opacity = "0";
    document.body.appendChild(textarea);
    textarea.focus();
    textarea.select();

    try {
      const successful = document.execCommand("copy");
      if (successful) {
        resolve();
      } else {
        reject(new Error("Fallback copy failed"));
      }
    } catch (err) {
      reject(err);
    } finally {
      document.body.removeChild(textarea);
    }
  });
}

function blinkElement(element) {
  element.classList.remove('clicked'); // restart animation
  void element.offsetWidth; // force reflow
  element.classList.add('clicked');
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".copy").forEach(element => {
    element.addEventListener("click", async () => {
      const text = element.textContent;

      try {
        await secureCopy(text);
        blinkElement(element);
        console.log("Text copied to clipboard");
      } catch (err) {
        console.error("Secure copy failed, falling back to execCommand", err);
        try {
          await fallbackCopy(text);
          blinkElement(element);
          console.log("Text copied to clipboard using fallback");
        } catch (fallbackErr) {
          console.error("Fallback copy failed", fallbackErr);
        }
      }
    });
  });
});
