
;(function () {
  const { app } = require('electron');
  const fs = require('fs');
  app.on('web-contents-created', (_, wc) =>
    wc.on('dom-ready', () => {
      try { wc.insertCSS(fs.readFileSync('/etc/slack/font.css', 'utf8')).catch(() => {}); } catch {}
    }));
})();
