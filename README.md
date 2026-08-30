# Shelf Scout

A phone-first personal tool for the Amazon Influencer Program: scout products you
already own, score them as video opportunities, generate talking-point outlines,
and track your video pipeline through Amazon's approval process.

## The workflow

1. **Identify** — photograph a product's label, drop it in a Claude chat with the
   built-in photo-ID prompt, and confirm the exact Amazon listing.
2. **Research** — read four numbers off the listing (best-seller rank, review
   count, star rating, video-carousel count); the app scores the opportunity
   (demand x per-sale earnings x video gap x rating) and gives a
   Film it / Maybe / Skip verdict with reasons.
3. **Outline** — generates a hook + beats + guardrails outline (no price talk,
   no health claims, honest drawback included — the top Amazon rejection reasons).
4. **Track** — pipeline statuses Idea → Filmed → Submitted → Live/Rejected, with
   a 3-approved-videos onsite-unlock progress bar and a rejection log.

## Source

Single-file app: `shelf-scout.html`. Published as a Claude artifact with the
`artifact` capability (state persists via `data/state.json` republish +
localStorage fallback) and `downloads` (JSON backup). The onsite commission-rate
table is editable in-app — the defaults are placeholders, not live Amazon data.
