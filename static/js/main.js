/**
* Template Name: Company
* Template URL: https://bootstrapmade.com/company-free-html-bootstrap-template/
* Updated: Aug 07 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Auto generate the carousel indicators
   */
  document.querySelectorAll('.carousel-indicators').forEach((carouselIndicator) => {
    carouselIndicator.closest('.carousel').querySelectorAll('.carousel-item').forEach((carouselItem, index) => {
      if (index === 0) {
        carouselIndicator.innerHTML += `<li data-bs-target="#${carouselIndicator.closest('.carousel').id}" data-bs-slide-to="${index}" class="active"></li>`;
      } else {
        carouselIndicator.innerHTML += `<li data-bs-target="#${carouselIndicator.closest('.carousel').id}" data-bs-slide-to="${index}"></li>`;
      }
    });
  });

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Init isotope layout and filters
   */
  document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {
    let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
    let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
    let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

    let initIsotope;
    imagesLoaded(isotopeItem.querySelector('.isotope-container'), function() {
      initIsotope = new Isotope(isotopeItem.querySelector('.isotope-container'), {
        itemSelector: '.isotope-item',
        layoutMode: layout,
        filter: filter,
        sortBy: sort
      });
    });

    isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filters) {
      filters.addEventListener('click', function() {
        isotopeItem.querySelector('.isotope-filters .filter-active').classList.remove('filter-active');
        this.classList.add('filter-active');
        initIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        if (typeof aosInit === 'function') {
          aosInit();
        }
      }, false);
    });

  });

  /**
   * Animate the skills items on reveal
   */
  let skillsAnimation = document.querySelectorAll('.skills-animation');
  skillsAnimation.forEach((item) => {
    new Waypoint({
      element: item,
      offset: '80%',
      handler: function(direction) {
        let progress = item.querySelectorAll('.progress .progress-bar');
        progress.forEach(el => {
          el.style.width = el.getAttribute('aria-valuenow') + '%';
        });
      }
    });
  });

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

})();

/* Metrics counter + reveal script (no libraries required) */
(function () {
  const section = document.getElementById('metrics');
  if (!section) return;

  const cols = Array.from(section.querySelectorAll('.col-md-3'));
  const counters = Array.from(section.querySelectorAll('.metric-value'));
  // helper: format big numbers with separators or short suffix handled outside
  function formatNumber(num) {
    if (num >= 1000000) return (num/1000000).toFixed(1).replace(/\.0$/, '') + 'M';
    if (num >= 1000) return (num/1000).toFixed(1).replace(/\.0$/, '') + 'k';
    return num.toString();
  }

  function animateCount(el, target, duration = 1400) {
    const start = 0;
    const range = target - start;
    const startTime = performance.now();
    function step(now) {
      const elapsed = Math.min((now - startTime) / duration, 1);
      const eased = 1 - Math.pow(1 - elapsed, 3); // easeOutCubic-ish
      const current = Math.floor(start + range * eased);
      // show scaled value: if target is large and original text used '2' with 'M+' suffix,
      // we do not change suffix — we update numeric portion only.
      el.textContent = (target >= 1000000 || target >= 1000) ? formatNumber(current) : current;
      if (elapsed < 1) requestAnimationFrame(step);
      else {
        // ensure final exact value
        el.textContent = (target >= 1000000 || target >= 1000) ? formatNumber(target) : target;
      }
    }
    requestAnimationFrame(step);
  }

  const onEnter = (entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // reveal columns with stagger
        cols.forEach((col, i) => {
          setTimeout(() => col.classList.add('in-view'), i * 120);
        });
        // start counters once
        counters.forEach((el, i) => {
          const target = parseInt(el.getAttribute('data-target') || el.textContent.replace(/\D/g,'') || 0, 10);
          // special case: if original content displayed '2' but suffix "M+" used, the target is set to 2000000 in HTML above
          animateCount(el, target);
        });
        obs.disconnect();
      }
    });
  };

  const io = new IntersectionObserver(onEnter, { threshold: 0.25 });
  io.observe(section);
})();

const swiper = new Swiper('.testimonials-slider', {
  slidesPerView: 1,
  spaceBetween: 20,
  loop: true,
  pagination: { 
    el: '.swiper-pagination', 
    clickable: true 
  },
  navigation: { 
    nextEl: '.swiper-button-next', 
    prevEl: '.swiper-button-prev' 
  },
  autoplay: { 
    delay: 4500, 
    disableOnInteraction: false 
  },
  breakpoints: { 
    768: { slidesPerView: 1 }, 
    992: { slidesPerView: 1 } 
  }
});

document.addEventListener('DOMContentLoaded', function () {
  const navToggle = document.querySelector('.mobile-nav-toggle');
  const body = document.querySelector('body');

  navToggle.addEventListener('click', function () {
    body.classList.toggle('mobile-nav-active');
  });

  // Optional: Close mobile menu when clicking a link
  document.querySelectorAll('.navmenu a').forEach(link => {
    link.addEventListener('click', () => {
      if (body.classList.contains('mobile-nav-active')) {
        body.classList.remove('mobile-nav-active');
      }
    });
  });
});

  (function () {
    // Mark body as preloading immediately (prevents scroll + ensures initial state)
    document.body.classList.add('preloading');

    // Record when the preloader started being visible
    const MIN_VISIBLE = 700; // 3 seconds
    const start = Date.now();

    function finish() {
      const elapsed = Date.now() - start;
      const remaining = Math.max(0, MIN_VISIBLE - elapsed);

      // Ensure the preloader stays for at least MIN_VISIBLE ms
      setTimeout(() => {
        document.body.classList.add('loaded');
        document.body.classList.remove('preloading');
      }, remaining);
    }

    // If the page is already fully loaded, finish immediately (but still respect MIN_VISIBLE)
    if (document.readyState === 'complete') {
      finish();
    } else {
      // On full load, finish (respecting MIN_VISIBLE)
      window.addEventListener('load', finish, { once: true });
    }

    // Absolute safety timeout (in case 'load' never fires due to blocked resources)
    setTimeout(() => {
      if (!document.body.classList.contains('loaded')) {
        document.body.classList.add('loaded');
        document.body.classList.remove('preloading');
      }
    }, 12000); // 12s hard cap
  })();