document.addEventListener('alpine:init', () => {
  Alpine.data('ministrySite', () => ({
    menuOpen: false,
    searchOpen: false,
    requestError: false,
    toggleSearch() {
      this.searchOpen = !this.searchOpen;
      if (this.searchOpen) this.$nextTick(() => this.$refs.searchInput.focus());
    },
    closePanels() {
      if (this.searchOpen) {
        this.searchOpen = false;
        this.$refs.searchToggle.focus();
      } else if (this.menuOpen) {
        this.menuOpen = false;
        this.$refs.menuToggle.focus();
      }
    },
  }));
});
