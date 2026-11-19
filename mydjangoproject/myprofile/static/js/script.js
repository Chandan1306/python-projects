
document.addEventListener("DOMContentLoaded", () => {

    // Mobile navigation
    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");
    const navItems = document.querySelectorAll(".nav-link");

    menuToggle.addEventListener("click", () => {
        navLinks.classList.toggle("open");
    });

    navItems.forEach(link => {
        link.addEventListener("click", () => {
            navLinks.classList.remove("open");
        });
    });

    // Typing animation
    const typingText = document.getElementById("typingText");

    const words = [
        "digital experiences.",
        "Python applications.",
        "IoT solutions.",
        "creative projects.",
        "practical solutions."
    ];

    let wordIndex = 0;
    let charIndex = 0;
    let deleting = false;

    function typeEffect() {
        const currentWord = words[wordIndex];

        if (deleting) {
            charIndex--;
        } else {
            charIndex++;
        }

        typingText.textContent = currentWord.substring(0, charIndex);

        let delay = deleting ? 45 : 90;

        if (!deleting && charIndex === currentWord.length) {
            deleting = true;
            delay = 1500;
        } else if (deleting && charIndex === 0) {
            deleting = false;
            wordIndex = (wordIndex + 1) % words.length;
            delay = 400;
        }

        setTimeout(typeEffect, delay);
    }

    typeEffect();

    // Scroll reveal animation
    const revealElements = document.querySelectorAll(".reveal");

    if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.12
        });

        revealElements.forEach(element => observer.observe(element));
    } else {
        revealElements.forEach(element => element.classList.add("visible"));
    }

    // Scroll progress bar
    const progressBar = document.getElementById("scrollProgress");

    function updateProgress() {
        const scrollTop = window.scrollY;
        const scrollHeight =
            document.documentElement.scrollHeight - window.innerHeight;

        const progress = scrollHeight > 0
            ? (scrollTop / scrollHeight) * 100
            : 0;

        progressBar.style.width = progress + "%";
    }

    window.addEventListener("scroll", updateProgress, { passive: true });
    updateProgress();

    // Active navigation link
    const sections = document.querySelectorAll("main section[id]");

    if ("IntersectionObserver" in window) {
        const sectionObserver = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    navItems.forEach(link => {
                        link.classList.toggle(
                            "active",
                            link.getAttribute("href") === "#" + entry.target.id
                        );
                    });
                }
            });
        }, {
            rootMargin: "-35% 0px -55% 0px"
        });

        sections.forEach(section => sectionObserver.observe(section));
    }

    // Contact form - opens the visitor's email application
    const contactForm = document.getElementById("contactForm");

    contactForm.addEventListener("submit", event => {
        event.preventDefault();

        const name = document.getElementById("visitorName").value.trim();
        const email = document.getElementById("visitorEmail").value.trim();
        const subject = document.getElementById("visitorSubject").value.trim();
        const message = document.getElementById("visitorMessage").value.trim();

        if (!name || !email || !subject || !message) {
            alert("Please fill in all fields.");
            return;
        }

        const recipient = "chandanchandanbn49@gmail.com";

        const mailSubject = encodeURIComponent(subject);
        const mailBody = encodeURIComponent(
            "Hello Chandan,\n\n" +
            message +
            "\n\nFrom: " + name +
            "\nEmail: " + email
        );

        window.location.href =
            `mailto:${recipient}?subject=${mailSubject}&body=${mailBody}`;
    });

    // Automatic footer year
    document.getElementById("currentYear").textContent =
        new Date().getFullYear();

});
