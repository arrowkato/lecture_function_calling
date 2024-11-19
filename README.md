# lecture_function_calling

## OpenAIとAnthropicのAPIキー
```bash
cp .env.sample .env

```
.env ファイルに OpenAI と AnthropicのAPIキーを記入してください。


## Google Cloud へのアクセス

```bash
# <PROJECT_ID> は、Google Cloud Platform のプロジェクトIDに置き換えてください。
export CLOUDSDK_CORE_PROJECT=<PROJECT_ID>

# コマンドを打つと、URLが出てくるので、認証して、パスワードっぽい長い文字列をコピペしてください
gcloud auth application-default login
```
