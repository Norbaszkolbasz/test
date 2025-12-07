# My Farm Game (minimal)

Ez egy nagyon egyszerű, konzolos farm játék példa.

Fájlok:
- `main.py` – futtatható belépési pont.
- `game/grid.py` – mezők és ültetés logikája.
- `game/crops.py` – növénymodell és sablonok.
- `game/shop.py` – egyszerű bolt (jelenleg csak váz).
- `game/ui.py` – konzolos megjelenítés.
- `assets/` – ikonok és csempék helye (helyőrzők).

Használat:

Futtatás:

```bash
python3 main.py
```

Parancsok a játékban:
- `p <seed> <x> <y>` – ültetés (pl. `p wheat_seed 1 2`).
- `h <x> <y>` – betakarítás.
- `t` – előre lépteti az időt (növekszik a növények kora).
- `q` – kilépés.
- `help` – súgó.

Megjegyzés: ez egy minimális vázlat — szívesen kibővítem GUI-val, mentéssel vagy több játékmeneti résszel, ha szeretnéd.
