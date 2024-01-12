import React, { Fragment, useState } from "react";
import { Dialog, Popover, Transition } from "@headlessui/react";
import ButtonPrimary from "shared/Button/ButtonPrimary";
import ButtonThird from "shared/Button/ButtonThird";
import ButtonClose from "shared/ButtonClose/ButtonClose";
import Checkbox from "shared/Checkbox/Checkbox";
import convertNumbThousand from "utils/convertNumbThousand";
import Slider from "rc-slider";

// DEMO DATA
const typeOfAirlines = [
  {
    name: "Jetstar Pacific Airlines",
  },
  {
    name: "Bamboo Airways",
  },
  {
    name: "Vietjet Air",
  },
  {
    name: "Vietnam Airlines",
  },
];

//
const TabFilters = () => {
  //
  const [airlinesStates, setAirlinesStates] = useState<string[]>([]);


  const handleChangeAirlines = (checked: boolean, name: string) => {
    checked
      ? setAirlinesStates([...airlinesStates, name])
      : setAirlinesStates(airlinesStates.filter((i) => i !== name));
  };


  const renderTabsTypeOfAirlines = () => {
    return (
      <Popover className="relative">
        {({ open, close }) => (
          <>
            <Popover.Button
              className={`flex items-center justify-center px-4 py-2 text-sm rounded-full border border-neutral-300 dark:border-neutral-700 hover:border-neutral-400 dark:hover:border-neutral-500 focus:outline-none
               ${open ? "!border-primary-500 " : ""}
                ${
                  !!airlinesStates.length
                    ? "!border-primary-500 bg-primary-50"
                    : ""
                }
                `}
            >
              <span>Hãng bay</span>
              {!airlinesStates.length ? (
                <i className="las la-angle-down ml-2"></i>
              ) : (
                <span onClick={() => setAirlinesStates([])}>
                </span>
              )}
            </Popover.Button>
            <Transition
              as={Fragment}
              enter="transition ease-out duration-200"
              enterFrom="opacity-0 translate-y-1"
              enterTo="opacity-100 translate-y-0"
              leave="transition ease-in duration-150"
              leaveFrom="opacity-100 translate-y-0"
              leaveTo="opacity-0 translate-y-1"
            >
              <Popover.Panel className="absolute z-10 w-screen max-w-sm px-4 mt-3 left-0 sm:px-0 lg:max-w-md">
                <div className="overflow-hidden rounded-2xl shadow-xl bg-white dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-700">
                  <div className="relative flex flex-col px-5 py-6 space-y-5">
                    <Checkbox
                      name="Tất cả"
                      label="Tất cả"
                      defaultChecked={airlinesStates.includes("Tất cả")}
                      onChange={(checked) =>
                        handleChangeAirlines(checked, "Tất cả")
                      }
                    />
                    <hr />
                    {typeOfAirlines.map((item) => (
                      <div key={item.name} className="">
                        <Checkbox
                          name={item.name}
                          label={item.name}
                          defaultChecked={airlinesStates.includes(item.name)}
                          onChange={(checked) =>
                            handleChangeAirlines(checked, item.name)
                          }
                        />
                      </div>
                    ))}
                  </div>
                  <div className="p-5 bg-neutral-50 dark:bg-neutral-900 dark:border-t dark:border-neutral-800 flex items-center justify-between">
                    <ButtonThird
                      onClick={() => {
                        close();
                        setAirlinesStates([]);
                      }}
                      sizeClass="px-4 py-2 sm:px-5"
                    >
                      Xóa
                    </ButtonThird>
                    <ButtonPrimary
                      onClick={close}
                      sizeClass="px-4 py-2 sm:px-5"
                    >
                      Áp dụng
                    </ButtonPrimary>
                  </div>
                </div>
              </Popover.Panel>
            </Transition>
          </>
        )}
      </Popover>
    );
  };

  return (
    <div className="flex lg:space-x-4">
      {/* FOR DESKTOP */}
      <div className="hidden lg:flex space-x-4">
        {renderTabsTypeOfAirlines()}
      </div>
    </div>
  );
};

export default TabFilters;
