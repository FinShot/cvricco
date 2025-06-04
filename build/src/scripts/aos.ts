// Initialize AOS with configuration
export function initAOS() {
  if (typeof window !== 'undefined') {
    import('aos').then((AOS) => {
      AOS.default.init({
        duration: 1000,
        once: true,
        disable: 'mobile'
      });
    });
  }
}