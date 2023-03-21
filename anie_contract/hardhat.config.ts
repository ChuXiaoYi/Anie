import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import "@nomiclabs/hardhat-etherscan";

require("dotenv").config();

const config: HardhatUserConfig = {
  defaultNetwork: "goerli",
  solidity: "0.8.18",
  networks: {
    hardhat: {},
    goerli: {
      url: "https://eth-goerli.g.alchemy.com/v2/Mv4c4nCBhsjFsDp770Vxg2XFjkrYU8w1",
      accounts: [
        process.env.PRIVATE_KEY1,
        process.env.PRIVATE_KEY2,
        process.env.PRIVATE_KEY3,
      ],
    },
    sepolia: {
      url: "https://eth-sepolia.g.alchemy.com/v2/ImKu6E0LMiYuO3gb-IKnb64T4m1NQJL1",
      accounts: [
        process.env.PRIVATE_KEY1,
        process.env.PRIVATE_KEY2,
        process.env.PRIVATE_KEY3,
      ],
    },
  },
  etherscan: {
    apiKey: process.env.ETHERSCAN_API_KEY,
  },
};

export default config;
