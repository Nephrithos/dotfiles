return {
	{
		"neovim/nvim-lspconfig",
		event = { "BufReadPre", "BufNewFile" },
		dependencies = {
			"hrsh7th/cmp-nvim-lsp",
			{ "antosha417/nvim-lsp-file-operations", config = true },
		},
	},
	{
		"williamboman/mason.nvim",
		config = function()
			require("mason").setup()
		end,
	},
	{
		"williamboman/mason-lspconfig.nvim",
		dependencies = { "mason.nvim" },
		config = function()
			local capabilities = require("cmp_nvim_lsp").default_capabilities()

			require("mason-lspconfig").setup()
			require("mason-lspconfig").setup_handlers({
				function(server_name)
					if server_name == "clangd" then
						require("lspconfig").clangd.setup({
							capabilities = capabilities,
							filetypes = {
								"c",
								"cpp",
							},
						})
					elseif server_name == "lua_ls" then
						require("lspconfig").lua_ls.setup({
							capabilities = capabilities,
							settings = {
								Lua = {
									diagnostics = {
										globals = { "vim" },
									},
									workspace = {
										-- make language server aware of runtime files
										library = {
											[vim.fn.expand("$VIMRUNTIME/lua")] = true,
											[vim.fn.stdpath("config") .. "/lua"] = true,
										},
									},
								},
							},
						})
					elseif server_name == "pylsp" then
						require("lspconfig").pylsp.setup({
							capabilities = capabilities,
							settings = {
								pylsp = {
									plugins = {
										jedi_completion = {
											enabled = true,
											include_params = true,
										},
									},
								},
							},
						})
					elseif server_name == "html" then
						require("lspconfig").html.setup({
							capabilities = capabilities,
						})
					elseif server_name == "cssls" then
						require("lspconfig").cssls.setup({
							capabilities = capabilities,
						})
					elseif server_name == "tailwindcss" then
						require("lspconfig").tailwindcss.setup({
							capabilities = capabilities,
						})
					elseif server_name == "graphql" then
						require("lspconfig").graphql.setup({
							capabilities = capabilities,
							filetypes = { "graphql", "gql", "svelte", "typescriptreact", "javascriptreact" },
						})
					elseif server_name == "emmet_ls" then
						require("lspconfig").emmet_ls.setup({
							capabilities = capabilities,
							filetypes = {
								"html",
								"typescriptreact",
								"javascriptreact",
								"css",
								"sass",
								"scss",
								"less",
								"svelte",
							},
						})
					else
						require("lspconfig")[server_name].setup({
							capabilities = capabilities,
						})
					end
				end,
			})
		end,
	},
}
