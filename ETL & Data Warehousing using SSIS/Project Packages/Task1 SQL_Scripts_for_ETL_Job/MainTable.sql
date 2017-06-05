USE [YAM]
GO

/****** Object:  Table [dbo].[MainTable]    Script Date: 14-03-2017 01:08:07 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[MainTable](
	[Category_ID] [int] NULL,
	[Item_ID] [int] NULL,
	[Serving_Size] [text] NOT NULL,
	[Calories] [text] NOT NULL,
	[Calories_from_Fat] [text] NOT NULL,
	[Total_Fat] [text] NOT NULL,
	[Total_Fat_Daily_Value] [text] NOT NULL,
	[Saturated_Fat] [text] NOT NULL,
	[Saturated_Fat_Daily_Value] [text] NOT NULL,
	[Trans_Fat] [text] NOT NULL,
	[Cholesterol] [text] NOT NULL,
	[Cholesterol_Daily_Value] [text] NOT NULL,
	[Sodium] [text] NOT NULL,
	[Sodium_Daily_Value] [text] NOT NULL,
	[Carbohydrates] [text] NOT NULL,
	[Carbohydrates_Daily_Value] [text] NOT NULL,
	[Dietary_Fiber] [text] NOT NULL,
	[Dietary_Fiber_Daily_Value] [text] NOT NULL,
	[Sugars] [text] NOT NULL,
	[Protein] [text] NOT NULL,
	[Vitamin_A_Daily_Value] [text] NOT NULL,
	[Vitamin_C_Daily_Value] [text] NOT NULL,
	[Calcium_Daily_Value] [text] NOT NULL,
	[Iron_Daily_Value] [text] NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

