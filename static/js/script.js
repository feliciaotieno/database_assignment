
// --- Confirm remove from cart ---
document.querySelectorAll(".remove-item-form").forEach(form => {
  form.addEventListener("submit", function (e) {
    if (!confirm("Are you sure you want to remove this item from the cart?")) {
      e.preventDefault();
    } else {
      
      const row = this.closest("tr");
      row.style.transition = "opacity 0.4s ease";
      row.style.opacity = "0";
    }
  });
});

// --- Auto-update cart total if quantities change ---
function updateCartTotal() {
  let total = 0;
  document.querySelectorAll(".subtotal").forEach(sub => {
    total += parseFloat(sub.textContent) || 0;
  });
  const totalEl = document.getElementById("cart-total");
  if (totalEl) {
    totalEl.textContent = total.toFixed(2);
  }
}

document.querySelectorAll(".qty-input").forEach(input => {
  input.addEventListener("input", function () {
    const price = parseFloat(this.dataset.price) || 0;
    const qty = parseInt(this.value) || 0;
    const subtotalEl = this.closest("tr").querySelector(".subtotal");
    const newSubtotal = price * qty;
    subtotalEl.textContent = newSubtotal.toFixed(2);
    updateCartTotal();
  });
});

// --- Checkout form validation ---
const checkoutForm = document.querySelector(".checkout-form form");
if (checkoutForm) {
  checkoutForm.addEventListener("submit", function (e) {
    let valid = true;

    
    this.querySelectorAll("[required]").forEach(input => {
      if (!input.value.trim()) {
        input.style.borderColor = "red";
        valid = false;
      } else {
        input.style.borderColor = "#ccc";
      }
    });

    // Email validation
    const emailField = this.querySelector("input[type='email']");
    if (emailField && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailField.value)) {
      emailField.style.borderColor = "red";
      valid = false;
    }

    if (!valid) {
      e.preventDefault();
      alert("Please fill in all required fields correctly.");
    }
  });

  // Live validation as user types
  checkoutForm.querySelectorAll("input, textarea").forEach(input => {
    input.addEventListener("input", function () {
      if (this.hasAttribute("required") && !this.value.trim()) {
        this.style.borderColor = "red";
      } else {
        this.style.borderColor = "#ccc";
      }
    });
  });
}

// --- Smooth scroll for nav links ---
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function (e) {
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: "smooth" });
    }
  });
});

// --- Lightbox for product images ---
document.querySelectorAll(".product-card img").forEach(img => {
  img.addEventListener("click", function () {
    
    const overlay = document.createElement("div");
    overlay.style.position = "fixed";
    overlay.style.top = "0";
    overlay.style.left = "0";
    overlay.style.width = "100%";
    overlay.style.height = "100%";
    overlay.style.background = "rgba(0,0,0,0.8)";
    overlay.style.display = "flex";
    overlay.style.justifyContent = "center";
    overlay.style.alignItems = "center";
    overlay.style.zIndex = "9999";

    // Large image
    const largeImg = document.createElement("img");
    largeImg.src = this.src;
    largeImg.style.maxWidth = "80%";
    largeImg.style.maxHeight = "80%";
    largeImg.style.borderRadius = "8px";
    largeImg.style.boxShadow = "0 4px 12px rgba(0,0,0,0.5)";
    overlay.appendChild(largeImg);

    overlay.addEventListener("click", () => overlay.remove());

    document.body.appendChild(overlay);
  });
});
