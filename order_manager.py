import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
from datetime import datetime

class OrderManager:
    def __init__(self, root):
        self.root = root
        self.root.title("订单管理系统")
        self.root.geometry("900x600")
        self.root.resizable(True, True)
        
        # 设置样式
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))
        self.style.configure("Treeview", font=('Arial', 9))
        
        # 创建数据库和表
        self.create_database()
        
        # 创建界面
        self.create_widgets()
        
        # 加载订单数据
        self.load_orders()
    
    def create_database(self):
        """创建数据库和订单表"""
        self.conn = sqlite3.connect('orders.db')
        self.cursor = self.conn.cursor()
        
        # 创建订单表
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_number TEXT NOT NULL UNIQUE,
            customer_name TEXT NOT NULL,
            order_date TEXT NOT NULL,
            total_amount REAL NOT NULL,
            status TEXT NOT NULL,
            description TEXT
        )
        ''')
        
        self.conn.commit()
    
    def create_widgets(self):
        """创建界面组件"""
        # 顶部按钮区域
        button_frame = ttk.Frame(self.root, padding=10)
        button_frame.pack(fill=tk.X)
        
        ttk.Button(button_frame, text="添加订单", command=self.add_order).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="修改订单", command=self.edit_order).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="删除订单", command=self.delete_order).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="刷新", command=self.load_orders).pack(side=tk.LEFT, padx=5)
        
        # 搜索区域
        search_frame = ttk.Frame(self.root, padding=10)
        search_frame.pack(fill=tk.X)
        
        ttk.Label(search_frame, text="搜索:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.search_var, width=30).pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="搜索", command=self.search_orders).pack(side=tk.LEFT, padx=5)
        
        # 订单列表区域
        list_frame = ttk.Frame(self.root, padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建树状视图
        columns = ("id", "订单编号", "客户名称", "订单日期", "总金额", "状态", "描述")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        # 设置列宽和标题
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "id":
                self.tree.column(col, width=50, anchor=tk.CENTER)
            elif col == "总金额":
                self.tree.column(col, width=80, anchor=tk.E)
            elif col == "描述":
                self.tree.column(col, width=200)
            else:
                self.tree.column(col, width=100, anchor=tk.CENTER)
        
        # 添加滚动条
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        # 布局树状视图和滚动条
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("就绪")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def load_orders(self):
        """从数据库加载所有订单"""
        # 清空现有数据
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # 查询所有订单
        self.cursor.execute("SELECT * FROM orders ORDER BY order_date DESC")
        orders = self.cursor.fetchall()
        
        # 添加到树状视图
        for order in orders:
            self.tree.insert("", tk.END, values=order)
        
        self.status_var.set(f"共显示 {len(orders)} 条订单")
    
    def search_orders(self):
        """搜索订单"""
        search_text = self.search_var.get().lower()
        
        # 清空现有数据
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # 搜索包含搜索文本的订单
        self.cursor.execute("SELECT * FROM orders WHERE "
                           "order_number LIKE ? OR "
                           "customer_name LIKE ? OR "
                           "description LIKE ?",
                           (f'%{search_text}%', f'%{search_text}%', f'%{search_text}%'))
        
        orders = self.cursor.fetchall()
        
        # 添加到树状视图
        for order in orders:
            self.tree.insert("", tk.END, values=order)
        
        self.status_var.set(f"搜索结果: {len(orders)} 条订单")
    
    def add_order(self):
        """添加新订单"""
        # 创建添加订单的对话框
        dialog = tk.Toplevel(self.root)
        dialog.title("添加订单")
        dialog.geometry("400x300")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # 创建输入字段
        fields = {}
        
        row = 0
        for label_text in ["订单编号:", "客户名称:", "总金额:", "状态:", "描述:"]:
            ttk.Label(dialog, text=label_text).grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)
            
            if label_text == "订单编号:":
                # 生成默认订单编号
                default_order_num = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
                fields[label_text] = ttk.Entry(dialog)
                fields[label_text].insert(0, default_order_num)
            elif label_text == "总金额:":
                fields[label_text] = ttk.Entry(dialog)
            elif label_text == "状态:":
                fields[label_text] = ttk.Combobox(dialog, values=["待处理", "已完成", "已取消"])
                fields[label_text].current(0)
            elif label_text == "描述:":
                fields[label_text] = tk.Text(dialog, height=4, width=30)
            else:
                fields[label_text] = ttk.Entry(dialog)
            
            if label_text == "描述:":
                fields[label_text].grid(row=row, column=1, padx=10, pady=5, sticky=tk.W)
            else:
                fields[label_text].grid(row=row, column=1, padx=10, pady=5, sticky=tk.W+tk.E)
            
            row += 1
        
        # 设置列权重，使输入框可以拉伸
        dialog.grid_columnconfigure(1, weight=1)
        
        # 添加按钮
        def save_order():
            try:
                order_number = fields["订单编号:"].get().strip()
                customer_name = fields["客户名称:"].get().strip()
                total_amount = float(fields["总金额:"].get().strip())
                status = fields["状态:"].get()
                description = fields["描述:"].get("1.0", tk.END).strip()
                order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # 验证必填字段
                if not order_number or not customer_name:
                    messagebox.showerror("错误", "订单编号和客户名称不能为空")
                    return
                
                # 插入数据库
                self.cursor.execute('''
                INSERT INTO orders (order_number, customer_name, order_date, total_amount, status, description)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', (order_number, customer_name, order_date, total_amount, status, description))
                
                self.conn.commit()
                messagebox.showinfo("成功", "订单添加成功")
                dialog.destroy()
                self.load_orders()
                
            except ValueError:
                messagebox.showerror("错误", "总金额必须是数字")
            except sqlite3.IntegrityError:
                messagebox.showerror("错误", "订单编号已存在")
            except Exception as e:
                messagebox.showerror("错误", f"添加订单失败: {str(e)}")
        
        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=row, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="保存", command=save_order).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="取消", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
        
        # 居中显示对话框
        dialog.update_idletasks()
        width = dialog.winfo_width()
        height = dialog.winfo_height()
        x = (self.root.winfo_width() // 2) - (width // 2) + self.root.winfo_x()
        y = (self.root.winfo_height() // 2) - (height // 2) + self.root.winfo_y()
        dialog.geometry(f"+{x}+{y}")
    
    def edit_order(self):
        """修改选中的订单"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("提示", "请先选择一个订单")
            return
        
        # 获取选中的订单数据
        order_data = self.tree.item(selected_item[0])['values']
        order_id = order_data[0]
        
        # 创建编辑订单的对话框
        dialog = tk.Toplevel(self.root)
        dialog.title("修改订单")
        dialog.geometry("400x300")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # 创建输入字段并填充现有数据
        fields = {}
        
        row = 0
        # 跳过ID字段，从订单编号开始
        labels = ["订单编号:", "客户名称:", "订单日期:", "总金额:", "状态:", "描述:"]
        for i, label_text in enumerate(labels, start=1):
            ttk.Label(dialog, text=label_text).grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)
            
            if label_text == "订单日期:":
                # 日期字段设为只读
                fields[label_text] = ttk.Entry(dialog, state="readonly")
                fields[label_text].insert(0, order_data[i])
                fields[label_text]['state'] = 'readonly'
            elif label_text == "总金额:":
                fields[label_text] = ttk.Entry(dialog)
                fields[label_text].insert(0, order_data[i])
            elif label_text == "状态:":
                fields[label_text] = ttk.Combobox(dialog, values=["待处理", "已完成", "已取消"])
                fields[label_text].set(order_data[i])
            elif label_text == "描述:":
                fields[label_text] = tk.Text(dialog, height=4, width=30)
                fields[label_text].insert("1.0", order_data[i] if i < len(order_data) else "")
            else:
                fields[label_text] = ttk.Entry(dialog)
                fields[label_text].insert(0, order_data[i])
            
            if label_text == "描述:":
                fields[label_text].grid(row=row, column=1, padx=10, pady=5, sticky=tk.W)
            else:
                fields[label_text].grid(row=row, column=1, padx=10, pady=5, sticky=tk.W+tk.E)
            
            row += 1
        
        # 设置列权重
        dialog.grid_columnconfigure(1, weight=1)
        
        # 保存修改的函数
        def update_order():
            try:
                order_number = fields["订单编号:"].get().strip()
                customer_name = fields["客户名称:"].get().strip()
                total_amount = float(fields["总金额:"].get().strip())
                status = fields["状态:"].get()
                description = fields["描述:"].get("1.0", tk.END).strip()
                
                # 验证必填字段
                if not order_number or not customer_name:
                    messagebox.showerror("错误", "订单编号和客户名称不能为空")
                    return
                
                # 更新数据库
                self.cursor.execute('''
                UPDATE orders SET 
                    order_number = ?, 
                    customer_name = ?, 
                    total_amount = ?, 
                    status = ?, 
                    description = ?
                WHERE id = ?
                ''', (order_number, customer_name, total_amount, status, description, order_id))
                
                self.conn.commit()
                messagebox.showinfo("成功", "订单更新成功")
                dialog.destroy()
                self.load_orders()
                
            except ValueError:
                messagebox.showerror("错误", "总金额必须是数字")
            except sqlite3.IntegrityError:
                messagebox.showerror("错误", "订单编号已存在")
            except Exception as e:
                messagebox.showerror("错误", f"更新订单失败: {str(e)}")
        
        # 添加按钮
        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=row, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="保存", command=update_order).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="取消", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
        
        # 居中显示对话框
        dialog.update_idletasks()
        width = dialog.winfo_width()
        height = dialog.winfo_height()
        x = (self.root.winfo_width() // 2) - (width // 2) + self.root.winfo_x()
        y = (self.root.winfo_height() // 2) - (height // 2) + self.root.winfo_y()
        dialog.geometry(f"+{x}+{y}")
    
    def delete_order(self):
        """删除选中的订单"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("提示", "请先选择一个订单")
            return
        
        # 获取选中的订单ID和编号
        order_data = self.tree.item(selected_item[0])['values']
        order_id = order_data[0]
        order_number = order_data[1]
        
        # 确认删除
        if messagebox.askyesno("确认", f"确定要删除订单 {order_number} 吗？"):
            try:
                # 从数据库删除
                self.cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
                self.conn.commit()
                messagebox.showinfo("成功", "订单已删除")
                self.load_orders()
            except Exception as e:
                messagebox.showerror("错误", f"删除订单失败: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderManager(root)
    root.mainloop()
