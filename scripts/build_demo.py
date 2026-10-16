#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["Pillow>=10.1"]
# ///
"""Regenerate the Ponyhead README terminal-demo GIF.

Run: uv run scripts/build_demo.py
No network or AI inference is involved.
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONTS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "C:/Windows/Fonts/CascadiaMono.ttf",  # Consolas has no U+2713
    "/System/Library/Fonts/Menlo.ttc",
]
BOLD_FONTS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    "C:/Windows/Fonts/consolab.ttf",
    "/System/Library/Fonts/Menlo.ttc",
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    for path in BOLD_FONTS if bold else FONTS:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)


def make_mascot() -> Image.Image:
    """Load the approved B avatar without re-cropping an older concept."""
    return Image.open(ASSETS / "ponyhead-avatar.png").convert("RGBA")


def make_frames(avatar: Image.Image) -> list[Image.Image]:
    W,H=990,390
    dark=(17,19,24); panel=(25,29,37); panel_border=(65,70,83)
    warm=(236,151,138); white=(240,241,244); muted=(155,164,178)
    line_color=(137,205,177); cyan=(115,199,225)
    line_font=font(24); title_font=font(22,True); small=font(18); note=font(20,True)
    left=["for i in range(1, 6):", "    print(i)"]
    right=["print(1)","print(2)","print(3)","print(4)","print(5)"]
    frames=[]
    stages=[0,1,2,3,4,5,5,5,5]
    durations=[400,420,450,430,430,450,500,500,850]
    for tick, stage in enumerate(stages):
        img=Image.new("RGB",(W,H),dark);d=ImageDraw.Draw(img)
        d.rounded_rectangle((18,18,972,308),radius=18,fill=panel,outline=panel_border,width=2)
        d.rounded_rectangle((18,18,972,69),radius=18,fill=(38,42,51))
        d.rectangle((18,49,972,70),fill=(38,42,51))
        for x,c in [(39,(236,118,112)),(59,(233,182,89)),(79,(105,186,135))]:
            d.ellipse((x,36,x+12,48),fill=c)
        d.text((125,34),"Ponyhead · anti-optimization demo",font=title_font,fill=white)
        d.line((494,85,494,301),fill=panel_border,width=2)
        d.text((51,104),"NORMAL",font=title_font,fill=cyan)
        d.text((530,104),"PONYHEAD",font=title_font,fill=warm)
        for i,s in enumerate(left):
            d.text((50,155+i*37),f"{i+1:>2}  ",font=small,fill=muted)
            d.text((108,155+i*37),s,font=line_font,fill=white if i==0 else line_color)
        for i,s in enumerate(right[:stage]):
            yy=154+i*31
            d.text((530,yy),f"{i+1:>2} ",font=small,fill=muted)
            d.text((582,yy),s,font=line_font,fill=line_color)
        if stage<5:
            yy=154+stage*31
            if tick%2==0:
                d.rounded_rectangle((583,yy+2,594,yy+25),radius=2,fill=warm)
        else:
            d.text((748,258),"✓ it works",font=small,fill=warm)
        d.text((45,331),"Same output. More lines. Zero shame.",font=note,fill=white)
        d.text((740,335),"NO LOOPS CLUB",font=small,fill=warm)
        # Mini avatar at right-top: delightful, but not distracting.
        mascot=avatar.copy();mascot.thumbnail((46,46),Image.Resampling.LANCZOS)
        img.paste(mascot,(897,20),mascot)
        img.info["duration"]=durations[tick]
        frames.append(img)
    return frames


def main():
    avatar=make_mascot()
    frames=make_frames(avatar)
    # GIF source is deterministic, and loops rather than uploading a video.
    frames[0].save(ASSETS/"ponyhead-demo.gif",format="GIF",save_all=True,append_images=frames[1:],duration=[x.info['duration'] for x in frames],loop=0,optimize=True)
    # Also provide a still for contexts that don't auto-play GIFs.
    frames[-1].save(ASSETS/"ponyhead-demo-still.png",optimize=True)
    print("Created", ASSETS/"ponyhead-demo.gif")

if __name__ == "__main__":
    main()
