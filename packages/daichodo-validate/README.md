# daichodo-validate

法人番号と適格請求書発行事業者の登録番号を検証します。依存関係なし、通信なし、APIキー不要。

Validate Japanese corporate numbers (法人番号) and qualified invoice
registration numbers (登録番号). Zero dependencies, no network, no API key.

```bash
pip install daichodo-validate
```

```python
from daichodo_validate import validate_registration_number

validate_registration_number("T1010001153225")
# ValidationResult(valid=True, corporate_number='1010001153225')
```

## 日本語

検査用数字の計算式は国税庁が公表している仕様に基づくため、サービスへの接続は不要です。

判定できるのは**形式として正しいか**であり、**実際に登録されているか**ではありません。
登録の有無や有効期間を確認するには [daichodo.com](https://daichodo.com) の API を
ご利用ください。

### チェックディジットは個人事業主にも適用されます

**チェックディジットは個人事業主の登録番号にも適用されます。** 実測して修正しました。
全件データ（2026年8月31日）と直近の差分、あわせて5,421,496件を検証した結果、
法人・個人事業主・人格のない社団等のすべてがチェックディジットを満たしました。
例外はゼロ件です。

```python
validate_registration_number("T1234567890123")
# ValidationResult(valid=False, reason='check digit is 1, expected 9',
#                  corporate_number=None)
```

個人事業主の13桁は法人番号ではありません（抽出した5万件のうち、法人番号登録簿に
存在したものはゼロ件）。しかし採番規則は同じで、チェックディジットは同様に成立します。
つまり**番号だけでは法人か個人事業主かを判別できません**。判別できるのは登録簿の
照会のみです。

0.1.0 はチェックディジットが合わない番号を「個人事業主だから」として有効扱いに
していました。実在する番号はすべてチェックディジットを満たすため、この扱いは
打ち間違いや架空の番号をすべて通してしまうものでした。

## English

The check-digit rules come from the National Tax Agency's published
specification, so this needs no service behind it.

It tells you whether a number is **well-formed** — not whether it is
**registered**. For registration status and validity dates you need the API at
[daichodo.com](https://daichodo.com).

### Sole traders are not exempt from the check digit

**Corrected in 0.2.0, by measurement.** Every registration number in the
register satisfies the check digit — corporations, sole traders and
人格のない社団等 alike. Counted over the 全件 of 2026-08-31 and the newest
差分: 5,421,496 numbers, **zero exceptions**.

```python
validate_registration_number("T1234567890123")
# ValidationResult(valid=False, reason='check digit is 1, expected 9',
#                  corporate_number=None)
```

A sole trader's 13 digits are *not* a 法人番号 — none of 50,000 sampled appear
in the corporate register — but they come from the same numbering scheme, so
the check digit holds. **The number alone cannot tell you whether it belongs to
a corporation or a sole trader.** Only a register lookup can.

0.1.0 returned `valid=True` when the check digit failed, excusing it as a sole
trader. Since every genuine number passes, that accepted every typo and every
fabrication instead. It is a breaking change for anyone who relied on the
permissive behaviour, which is why this is 0.2.0 and not 0.1.1.

## ライセンス / Licence

MIT.

---

出典：国税庁法人番号公表サイト（国税庁）（https://www.houjin-bangou.nta.go.jp/）を加工して作成
