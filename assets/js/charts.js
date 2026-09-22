/* Minimal dependency-free SVG charts for calculator results. */
(function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  function fmt(n) {
    var a = Math.abs(n);
    if (a >= 1e9) return "$" + (n / 1e9).toFixed(1) + "B";
    if (a >= 1e6) return "$" + (n / 1e6).toFixed(a >= 1e7 ? 0 : 1) + "M";
    if (a >= 1e3) return "$" + (n / 1e3).toFixed(a >= 1e5 ? 0 : 1) + "k";
    return "$" + Math.round(n);
  }
  function legend(items) {
    return '<div class="legend">' + items.map(function (i) {
      return '<span><i style="background:' + i.color + '"></i>' + i.label + (i.value !== undefined ? " · " + i.value : "") + "</span>";
    }).join("") + "</div>";
  }

  /* donut(el, [{label, value, color}], centerLabel) */
  function donut(el, parts, center) {
    if (!el) return;
    parts = parts.filter(function (p) { return p.value > 0 && isFinite(p.value); });
    var total = parts.reduce(function (s, p) { return s + p.value; }, 0);
    if (!total) { el.innerHTML = ""; return; }
    var r = 42, c = 2 * Math.PI * r, off = 0, arcs = "";
    parts.forEach(function (p) {
      var len = p.value / total * c;
      arcs += '<circle r="' + r + '" cx="60" cy="60" fill="none" stroke="' + p.color + '" stroke-width="16" stroke-dasharray="' +
        len + " " + (c - len) + '" stroke-dashoffset="' + (-off) + '" transform="rotate(-90 60 60)"/>';
      off += len;
    });
    var pct = function (v) { return Math.round(v / total * 100) + "%"; };
    el.innerHTML = '<div class="donut-wrap"><svg viewBox="0 0 120 120" role="img" aria-label="Breakdown chart">' + arcs +
      (center ? '<text x="60" y="64" text-anchor="middle" font-size="13" font-weight="700" fill="#0b3f35">' + center + "</text>" : "") +
      "</svg>" + legend(parts.map(function (p) { return { label: p.label, color: p.color, value: pct(p.value) }; })) + "</div>";
  }

  /* area(el, labels[], sets[{label, color, values[]}]) — stacked area over time */
  function area(el, labels, sets) {
    if (!el || !labels.length) return;
    var W = 320, H = 170, L = 38, B = 22, T = 8, R = 6, n = labels.length;
    var totals = labels.map(function (_, i) { return sets.reduce(function (s, st) { return s + Math.max(0, st.values[i] || 0); }, 0); });
    var max = Math.max.apply(null, totals.concat([1]));
    if (!isFinite(max)) { el.innerHTML = ""; return; }
    var x = function (i) { return L + (n === 1 ? 0 : i / (n - 1) * (W - L - R)); };
    var y = function (v) { return T + (1 - v / max) * (H - T - B); };
    var svg = "", base = labels.map(function () { return 0; });
    // grid
    for (var g = 0; g <= 3; g++) {
      var gv = max * g / 3, gy = y(gv);
      svg += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + gy + '" y2="' + gy + '" stroke="#e7ecea"/>' +
        '<text x="' + (L - 5) + '" y="' + (gy + 3) + '" text-anchor="end" font-size="9" fill="#8a9893">' + fmt(gv) + "</text>";
    }
    sets.forEach(function (st) {
      var top = base.map(function (b, i) { return b + Math.max(0, st.values[i] || 0); });
      var d = "M" + x(0) + " " + y(top[0]);
      for (var i = 1; i < n; i++) d += " L" + x(i) + " " + y(top[i]);
      for (var j = n - 1; j >= 0; j--) d += " L" + x(j) + " " + y(base[j]);
      svg += '<path d="' + d + ' Z" fill="' + st.color + '" fill-opacity=".85"/>';
      base = top;
    });
    var step = Math.max(1, Math.ceil(n / 6));
    for (var k = 0; k < n; k += step) svg += '<text x="' + x(k) + '" y="' + (H - 6) + '" text-anchor="middle" font-size="9" fill="#8a9893">' + labels[k] + "</text>";
    if ((n - 1) % step) svg += '<text x="' + x(n - 1) + '" y="' + (H - 6) + '" text-anchor="end" font-size="9" fill="#8a9893">' + labels[n - 1] + "</text>";
    el.innerHTML = '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="Growth over time chart">' + svg + "</svg>" +
      legend(sets.map(function (s) { return { label: s.label, color: s.color }; }));
  }

  window.CMFChart = { donut: donut, area: area, colors: { brand: "#0f5c4d", brand2: "#2bb58f", gold: "#f2b441", slate: "#7fa99c", coral: "#e0724f", indigo: "#6366f1", sky: "#38bdf8" } };
})();
