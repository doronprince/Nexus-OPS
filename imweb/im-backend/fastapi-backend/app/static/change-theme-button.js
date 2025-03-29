import { Pane } from 'https://cdn.skypack.dev/tweakpane@4.0.4';

const config = {
    theme: 'dark',
};

const ctrl = new Pane({
    title: 'Config',
    expanded: true,
});

const update = () => {
    document.documentElement.dataset.theme = config.theme;
};

const sync = () => {
    update();
};

const toggleLogo = document.querySelector('.toggle-logo');

ctrl
    .addBinding(config, 'theme', {
        label: 'Theme',
        options: {
            System: 'system',
            Light: 'light',
            Dark: 'dark',
        },
    })
    .on('change', () => {
        toggleLogo.setAttribute('aria-pressed', config.theme === 'light');
    });

ctrl.on('change', sync);
update();

const handleToggle = () => {
    const light = !!toggleLogo.matches('[aria-pressed="false"]');
    toggleLogo.setAttribute('aria-pressed', light);
    config.theme = light ? 'light' : 'dark';
    ctrl.refresh();

    // Navigate to the dashboard
    window.location.href = 'im.html'; // Update with your dashboard URL
};

toggleLogo.addEventListener('click', handleToggle);
