import React, { FC, useState } from "react";
import { Helmet } from "react-helmet";
import Input from "shared/Input/Input";
import ButtonPrimary from "shared/Button/ButtonPrimary";
import { Link } from "react-router-dom";

export interface PageSignUpProps {
  className?: string;
}

const PageSignUp: FC<PageSignUpProps> = ({ className = "" }) => {
  // Sử dụng useState để theo dõi giá trị của password và confirm password
  const [password, setPassword] = useState<string>("");
  const [confirmPassword, setConfirmPassword] = useState<string>("");
  const [passwordError, setPasswordError] = useState<string | null>(null);

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
    // Kiểm tra sự trùng khớp khi mật khẩu thay đổi
    setPasswordError(
      event.target.value !== confirmPassword ? "Password does not match" : null
    );
  };

  const handleConfirmPasswordChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setConfirmPassword(event.target.value);
    // Kiểm tra sự trùng khớp khi mật khẩu xác nhận thay đổi
    setPasswordError(
      password !== event.target.value ? "Password does not match" : null
    );
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    // Kiểm tra nếu có lỗi về mật khẩu thì không tiếp tục
    if (passwordError) {
      return;
    }
    // Tiếp tục xử lý khi mọi thứ đều hợp lệ
    // ...

    console.log("Continue with the submission");
  };

  return (
    <div className={`nc-PageSignUp ${className}`} data-nc-id="PageSignUp">
      <Helmet>
        <title>Explore</title>
      </Helmet>
      <div className="container mb-24 lg:mb-32">
        <h2 className="my-20 flex items-center text-3xl leading-[115%] md:text-5xl md:leading-[115%] font-semibold text-neutral-900 dark:text-neutral-100 justify-center">
          Đăng ký
        </h2>
        <div className="max-w-md mx-auto space-y-6 ">
          <form className="grid grid-cols-1 gap-6" onSubmit={handleSubmit}>
            <label className="block">
              <span className="text-neutral-800 dark:text-neutral-200">
                Địa chỉ Email
              </span>
              <Input
                type="email"
                placeholder=""
                className="mt-1"
              />
            </label>
            <label className="block">
              <span className="flex justify-between items-center text-neutral-800 dark:text-neutral-200">
                Mật khẩu
              </span>
              <Input
                type="password"
                value={password}
                onChange={handlePasswordChange}
                className="mt-1"
              />
            </label>
            <label className="block">
              <span className="flex justify-between items-center text-neutral-800 dark:text-neutral-200">
                Xác nhận mật khẩu
              </span>
              <Input
                type="password"
                value={confirmPassword}
                onChange={handleConfirmPasswordChange}
                className="mt-1"
              />
              {/* Hiển thị thông báo lỗi nếu có */}
              {passwordError && (
                <p className="text-red-500 text-sm">{passwordError}</p>
              )}
            </label>
            <ButtonPrimary type="submit">Tiếp tục</ButtonPrimary>
          </form>

          <span className="block text-center text-neutral-700 dark:text-neutral-300">
            Đã có tài khoản? <Link to="/login">Đăng nhập</Link>
          </span>
        </div>
      </div>
    </div>
  );
};

export default PageSignUp;
