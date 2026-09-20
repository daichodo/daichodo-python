# daichodo

台帳堂は、日本の公的登録簿のための API です。本パッケージはその Python
クライアントで、適格請求書発行事業者（インボイス）登録番号と法人番号を照会します。

Daichodo is the ledger API for Japanese regulatory registers. This is its
Python client — qualified invoice issuer (適格請求書発行事業者) and corporate
number (法人番号) lookup, validation, and point-in-time validity.

> **APIキーは [app.daichodo.com](https://app.daichodo.com/ja/) ですぐに発行
> できます。** 無料プランはカード不要です。
>
> Create an API key at [app.daichodo.com](https://app.daichodo.com/en/) — free
> tier, no card, issued instantly.
>
> **APIキーが不要な検証だけであれば
> [`daichodo-validate`](https://pypi.org/project/daichodo-validate/)
> が今すぐ利用できます。**
> If you only need format and check-digit validation,
> [`daichodo-validate`](https://pypi.org/project/daichodo-validate/) works today
> with no API key.

```bash
pip install daichodo
```

```python
from daichodo import AuthenticatedClient
from daichodo.api.registry import get_invoice_issuer

client = AuthenticatedClient(
    base_url="https://api.daichodo.com",
    token="dc_live_...",
)

issuer = get_invoice_issuer.sync(client=client, registration_number="T1010001153225")
```

## `name` が None でもエラーではありません / `name` is None for sole traders

国税庁は個人事業主の氏名・住所を公表データから除外しています。個人事業主のレコードは
日付を保持したまま**氏名が None** で返ります。`name is None` を「該当なし」と解釈する
のが最も多い誤りで、登録簿の約半数を無言で切り捨てることになります。

The NTA strips identity fields for individuals at source, so a sole trader
returns their dates with **no name**. Treating `name is None` as "not found" is
the most common way to get this wrong, and it silently discards about half the
register.

## 生成コードです / This code is generated

API の OpenAPI スキーマから自動生成され、リリースごとに上書きされます。
プルリクエストは受け付けられません。不具合は
[Issue](https://github.com/daichodo/daichodo-python/issues) でご報告ください。

Generated from the API's OpenAPI schema and overwritten on every release.

## ライセンス / Licence

MIT.
