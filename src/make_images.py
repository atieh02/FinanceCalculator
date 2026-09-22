"""Generate favicons + Open Graph share images. Needs Pillow:  python src/make_images.py"""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
from content import CALCULATORS, CATEGORIES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
os.makedirs(os.path.join(IMG, "og"), exist_ok=True)
BRAND, BRAND_DARK, GOLD = (15, 92, 77), (11, 63, 53), (242, 180, 65)
CAT_COLORS = {"grow": (21, 128, 61), "retire": (180, 83, 9), "plan": (79, 70, 229)}
CAT_NAMES = {k: n for k, n, _ in CATEGORIES}


def font(size, bold=True):
    for name in (("segoeuib.ttf", "arialbd.ttf") if bold else ("segoeui.ttf", "arial.ttf")):
        p = os.path.join(r"C:\Windows\Fonts", name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def logo(size):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    s = size / 32
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=int(9 * s), fill=BRAND)
    pts = [(9 * s, 21.5 * s), (14 * s, 16 * s), (17.5 * s, 19.5 * s), (23 * s, 12 * s)]
    d.line(pts, fill="white", width=max(2, int(2.6 * s)), joint="curve")
    r = 2.3 * s
    d.ellipse([23 * s - r, 12 * s - r, 23 * s + r, 12 * s + r], fill=GOLD)
    return im


def icons():
    for size, name in ((32, "favicon-32.png"), (180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")):
        big = logo(size * 4).resize((size, size), Image.LANCZOS)
        if name == "apple-touch-icon.png":  # iOS ignores transparency; give it a solid background
            bg = Image.new("RGB", (size, size), BRAND)
            bg.paste(big, (0, 0), big)
            big = bg
        big.save(os.path.join(IMG, name))


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def og(name, title, subtitle, color):
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), BRAND_DARK)
    # soft gradient + glow
    grad = Image.new("RGB", (W, H))
    gd = ImageDraw.Draw(grad)
    for x in range(W):
        t = x / W
        gd.line([(x, 0), (x, H)], fill=tuple(int(BRAND_DARK[i] * (1 - t) + BRAND[i] * t) for i in range(3)))
    im.paste(grad)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([W - 520, -320, W + 200, 320], fill=GOLD + (70,))
    im.paste(glow.filter(ImageFilter.GaussianBlur(90)), (0, 0), glow.filter(ImageFilter.GaussianBlur(90)))
    d = ImageDraw.Draw(im)
    # brand
    lg = logo(256).resize((64, 64), Image.LANCZOS)
    im.paste(lg, (72, 64), lg)
    d.text((152, 70), "CalcMyFin", font=font(44), fill="white")
    # category pill
    if color:
        pill_font = font(26)
        label = subtitle.upper()
        tw = d.textlength(label, font=pill_font)
        d.rounded_rectangle([72, 190, 72 + tw + 40, 236], radius=23, fill=color)
        d.text((92, 195), label, font=pill_font, fill="white")
    # title
    tf = font(84 if len(title) < 26 else 70)
    y = 262 if color else 210
    for line in wrap(d, title, tf, W - 150)[:3]:
        d.text((72, y), line, font=tf, fill="white")
        y += int(tf.size * 1.12)
    tagline = "Free · Private · Shows the math" if color else subtitle
    d.text((72, H - 96), tagline, font=font(32, bold=False), fill=(214, 236, 230))
    d.rectangle([0, H - 12, W, H], fill=GOLD)
    im.save(os.path.join(IMG, "og", name + ".png"), optimize=True)


if __name__ == "__main__":
    icons()
    og("home", "Free financial calculators that show their math", "Investing · Retirement · 401(k) · Savings · Budget", None)
    for c in CALCULATORS:
        og(c["slug"], c["h1"], CAT_NAMES[c["cat"]], CAT_COLORS[c["cat"]])
    print("images written to", IMG)
