# 料金オプション

<!-- jinja -->
<table class="table table-bordered table-hover">
	<thead>
		<tr>
			<th rowspan=2 style="width: 40%;">プラン</th>
			<th colspan=2 class="text-center">インド以外の国</th>
			<th rowspan=2 class="text-right">インド</th>
		</tr>
		<tr>
			<th class="text-right">Paypal経由</th>
			<th class="text-right">Wire Transfer経由</th>
		</tr>
	</thead>
	<tbody>
		{% for plan in [
			{"name": "5 users, 5GB space", "name_ja": "5ユーザー・容量5GB", "usd": "$ 300"},
			{"name": "25 users, 10GB space", "name_ja": "25ユーザー・容量10GB", "usd": "$ 600"},
			{"name": "100 users, 20GB space", "name_ja": "100ユーザー・容量20GB", "usd": "$ 1500"},
			{"name": "Unlimited users, 50GB space", "name_ja": "ユーザー数無制限・容量50GB", "usd": "$ 3000"},
			{"name": "Single Instance Server Support", "name_ja": "シングルインスタンスサーバー サポート", "usd": "$ 1000"},
			{"name": "Multitenant Server Support", "name_ja": "マルチテナントサーバー サポート", "usd": "$ 3000"},
			{"name": "Assisted Development", "name_ja": "開発補助", "usd": "$ 5000"},
			{"name": "Developer Training", "name_ja": "開発者トレーニング", "usd": "$ 1500"},
			{"name": "User Training", "name_ja": "ユーザートレーニング", "usd": "$ 1500"},
			{"name": "Sponsorship", "name_ja": "スポンサーシップ", "usd": "$ 5000"},
		] -%}
			{% set inr = frappe.utils.fmt_money(
				frappe.utils.cint(frappe.utils.flt(frappe.utils.flt(plan.usd[1:]) * 60.0 * 1.1236 / 1000.0, 0) * 1000),
				precision=0,
				currency="INR") %}
			<tr>
				<td>{{ plan.name_ja }}</td>
				<td class="text-right"><a class="paypal-paynow" data-plan="{{ plan.name }}" onclick="pay.paypal(this)">{{ plan.usd }}</a></td>
				<td class="text-right"><a class="wire-transfer" data-amount="{{ plan.usd }}" onclick="pay.wire_transfer(this, '.wire-transfer-msg')">{{ plan.usd }}</a></td>
				<td class="text-right"><a class="india-wire-transfer" data-amount="{{ inr }}" onclick="pay.wire_transfer(this, '.india-wire-transfer-msg')">{{ inr }}</a></td>
			</tr>
		{%- endfor %}
	</tbody>
</table>

<div class="wire-transfer-msg hidden">
	<table class="table table-bordered table-hover">
		<tbody>
			<tr>
				<td width="30%">Name of Bank</td>
				<td>HDFC Bank Ltd.</td>
			</tr>
			<tr>
				<td>Address of Bank</td>
				<td>1st Floor, Sanghavi Square, M. G. Road, Ghatkopar (W), Mumbai - 400086, India.</td>
			</tr>
			<tr>
				<td>Account Number</td>
				<td>01632320001931</td>
			</tr>
			<tr>
				<td>Account Name (Beneficiary Name)</td>
				<td>Frappe Technologies Pvt. Ltd.</td>
			</tr>
			<tr>
				<td>IFSC Code</td>
				<td>HDFC0001473</td>
			</tr>
			<tr>
				<td>SWIFT Code</td>
				<td>HDFCINBBXXX</td>
			</tr>
		</tbody>
	</table>
	<hr>
	<h4>Note:</h4>
	<ul>
		<li>Bank and transfer charges are to be borne by you.</li>
		<li>Please notify us with your transaction id when you are sending a payment so that we can update your account.</li>
	</ul>
</div>

<div class="india-wire-transfer-msg hidden">
	<p>14% Service Tax is included for Indian Customers.</p>

	<hr>
	<h4>Option A: Direct Transfer</h4>
	<p>You can directly remit the amount to our bank. All bank transfer charges, if any, are to be borne by you.</p>
	<table class="table table-bordered table-hover">
		<tbody>
			<tr>
				<td width="30%">Name of Bank</td>
				<td>HDFC Bank Ltd.</td>
			</tr>
			<tr>
				<td>Address of Bank</td>
				<td>1st Floor, Sanghavi Square, M. G. Road, Ghatkopar (W), Mumbai - 400086, India.</td>
			</tr>
			<tr>
				<td>Account Number</td>
				<td>01632320001931</td>
			</tr>
			<tr>
				<td>Account Name (Beneficiary Name)</td>
				<td>Frappe Technologies Pvt. Ltd.</td>
			</tr>
			<tr>
				<td>IFSC Code</td>
				<td>HDFC0001473</td>
			</tr>
			<tr>
				<td>SWIFT Code</td>
				<td>HDFCINBBXXX</td>
			</tr>
		</tbody>
	</table>

	<hr>
	<h4>Option B: Deposit Cash / Check</h4>
	<p>You can also directly deposit a check to your local HDFC Bank Branch to our account:</p>
	<table class="table table-bordered table-hover">
		<tbody>
			<tr>
				<td width="30%">Payable To</td>
				<td>Frappe Technologies Pvt. Ltd.</td>
			</tr>
			<tr>
				<td>Account Number</td>
				<td>01632320001931</td>
			</tr>
		</tbody>
	</table>

	<hr>
	<h4>Option C: Mail / Courier Us A Check</h4>
	<p>You can send us your check by courier at:</p>
	<p>
		<b>Frappe Technologies Pvt Ltd.</b> <br>
		D - 324, Neelkanth Business Park, <br>
		Next to Vidyavihar Station, <br>
		Vidyavihar West, <br>
		Mumbai 400 086.
	</p>

	<hr>
	<h4>Note:</h4>
	<ul>
		<li>Bank and transfer charges are to be borne by you.</li>
		<li>Please notify us with your transaction id when you are sending a payment so that we can update your account.</li>
	</ul>
</div>
