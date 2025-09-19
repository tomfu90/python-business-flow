#coding =utf-8
# author =fufu
# day1 -最简单资金核对

# 模拟系统记录的金额
system_balance = 1000

# 模拟渠道流水（微信、支付宝、银行卡等）
channel_transactions = [500,200,300,100]

# 计算渠道总和
calculated_balance = sum(channel_transactions)

#比对

if calculated_balance == system_balance:
    print('✅ 资金平衡！系统余额与渠道流水一致。')
else:
    diff = abs(calculated_balance-system_balance)
    print(f'❌资金差值！差额：{diff}')
    print(f'系统余额：{system_balance}')
    print(f'渠道总和：{calculated_balance}')