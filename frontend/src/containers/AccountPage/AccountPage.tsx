import Label from "components/Label/Label";
import React, { FC } from "react";
import Avatar from "shared/Avatar/Avatar";
import ButtonPrimary from "shared/Button/ButtonPrimary";
import Input from "shared/Input/Input";
import Select from "shared/Select/Select";
import CommonLayout from "./CommonLayout";
import { Helmet } from "react-helmet";

export interface AccountPageProps {
  className?: string;
}

const AccountPage: FC<AccountPageProps> = ({ className = "" }) => {
  return (
    <div className={`nc-AccountPage ${className}`} data-nc-id="AccountPage">
      <Helmet>
        <title>Explore</title>
      </Helmet>
      <CommonLayout>
        <div className="space-y-6 sm:space-y-8">
          {/* HEADING */}
          <h2 className="text-3xl font-semibold">Thông tin tài khoản</h2>
          <div className="w-14 border-b border-neutral-200 dark:border-neutral-700"></div>
          <div className="flex flex-col md:flex-row">
            <div className="flex-grow mt-10 md:mt-0 md:pl-16 max-w-3xl space-y-6">
              <div>
                <Label>Tên</Label>
                <Input className="mt-1.5" defaultValue="Lê Trường Giang" />
              </div>
              {/* ---- */}
              <div>
                <Label>Giới tính</Label>
                <Select className="mt-1.5">
                  <option value="Male">Nam</option>
                  <option value="Female">Nữ</option>
                  <option value="Other">Khác</option>
                </Select>
              </div>
              {/* ---- */}
              {/* <div>
                <Label>Username</Label>
                <Input className="mt-1.5" defaultValue="@user" />
              </div> */}
              {/* ---- */}
              <div>
                <Label>Email</Label>
                <Input className="mt-1.5" defaultValue="letruonggiang7gpl@gmail.com" />
              </div>
              {/* ---- */}
              <div className="max-w-lg">
                <Label>Ngày sinh</Label>
                <Input
                  className="mt-1.5"
                  type="date"
                  defaultValue="2003-11-15"
                />
              </div>
              {/* ---- */}
              <div>
                <Label>Địa chỉ</Label>
                <Input className="mt-1.5" defaultValue="HN" />
              </div>
              {/* ---- */}
              <div>
                <Label>Số điện thoại</Label>
                <Input className="mt-1.5" defaultValue="0123456" />
              </div>
              {/* ---- */}
              <div className="pt-2">
                <ButtonPrimary>Cập nhật</ButtonPrimary>
              </div>
            </div>
          </div>
        </div>
      </CommonLayout>
    </div>
  );
};

export default AccountPage;
