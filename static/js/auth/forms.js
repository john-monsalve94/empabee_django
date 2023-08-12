function nextSection(nextIndex) {
    const currentSection = document.querySelector(".form-section.active");
    currentSection.classList.remove("active");

    const nextSection = document.getElementById(`section-${nextIndex}`);
    nextSection.classList.add("active");
}

function prevSection(prevIndex) {
    const currentSection = document.querySelector(".form-section.active");
    currentSection.classList.remove("active");

    const prevSection = document.getElementById(`section-${prevIndex}`);
    prevSection.classList.add("active");
}
