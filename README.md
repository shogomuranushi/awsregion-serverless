awsregion
====

## Description
awsのリージョン名（オレゴンなど）と略称（us-west-2など）を一覧表示するだけの機能

## Demo

```
$ ar
us-east-1       米国東部（バージニア北部）
us-west-2       米国西部（オレゴン）
us-west-1       米国西部（北カリフォルニア）
eu-west-1       欧州（アイルランド）
eu-central-1    欧州（フランクフルト）
ap-southeast-1  アジアパシフィック（シンガポール）
ap-northeast-1  アジアパシフィック（東京）
ap-southeast-2  アジアパシフィック（シドニー）
ap-northeast-2  アジアパシフィック (ソウル)
ap-south-1      アジアパシフィック (ムンバイ)
sa-east-1       南米 (サンパウロ)
```

## Usage

```
ar
```

## Install

```
alias ar="curl https://wnmotkdo1d.execute-api.us-east-1.amazonaws.com/dev/regions"
```

## create

```
curl -X POST -H "Content-Type: application/json" -H "Cache-Control: no-cache" -d '{
	"region": "sa-east-1",
	"jpname": "南米 (サンパウロ)"
}' "https://wnmotkdo1d.execute-api.us-east-1.amazonaws.com/dev/regions"
```

## read

```
curl -X GET https://wnmotkdo1d.execute-api.us-east-1.amazonaws.com/dev/regions
```

## update

## delete
